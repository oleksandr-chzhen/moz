import os
from datetime import datetime, timedelta

from flask import render_template, Blueprint, current_app, send_from_directory, request, make_response, abort
from flask_login import login_required, current_user

from config import PROTOCOL, DOMAIN
from moz import app
from moz.auth.email import check_confirmed
from services import get_categories_with_documents, get_documents_for_query, is_user_admin, get_document_by_id

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')


@main.route('/log')
@login_required
def download_log():
    if not is_user_admin(current_user):
        abort(404)
    return send_from_directory(app.config['LOGGING_FOLDER'], app.config['LOGGING_FILENAME'])


@main.route('/documents')
@login_required
@check_confirmed
def documents_list():
    categories_with_documents = get_categories_with_documents()
    current_app.logger.info("Found categories with documents %s for template documents_list.html",
                            categories_with_documents)
    return render_template('documents_list.html', categories=categories_with_documents)


@main.route('/documents/<id>')
@login_required
@check_confirmed
def document(id):
    if not id:
        abort(404)
    folder = os.path.join(app.config.get('MEDIA_ROOT'), 'moz')
    document = get_document_by_id(id)
    if not document:
        abort(404)
    current_app.logger.info("Looking for file %s in folder %s", document.file, folder)
    return send_from_directory(folder, document.file)


@main.route('/search')
@login_required
@check_confirmed
def search():
    query = request.args.get('query')
    query = query if query else ""
    query = u"%s" % query
    categories_with_documents = get_documents_for_query(query)
    current_app.logger.info(u"Found documents: %s for query: %s", categories_with_documents, query)
    return render_template('search.html', query=query, categories=categories_with_documents)


@main.route('/terms_of_use')
def terms_of_use():
    return render_template('terms_of_use.html')


@main.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
        pages = []
        ten_days_ago = (datetime.now() - timedelta(days=7)).date().isoformat()
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and len(rule.arguments) == 0 and 'admin' not in rule.rule:
                pages.append(
                    [PROTOCOL + DOMAIN + str(rule.rule), ten_days_ago]
                )

        sitemap_xml = render_template('sitemap_template.xml', pages=pages)
        response = make_response(sitemap_xml)
        response.headers["Content-Type"] = "application/xml"

        return response
    except Exception as e:
        return str(e)


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
