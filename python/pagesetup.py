#!/usr/bin/env python


def print_cgi_header():
    """Print out the required CGI header"""
    print "Content-Type: text/html"
    print ""


def print_head(title=""):
    """Print the standard page head
    :param title: The title to be displayed in the title bar or tab of the browser
    """
    print """
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Manage your Steam game backlog">
        <meta name="keywords" content="Steam,PC,Backlog,Games">
        <meta name="author" content="Graydon Armstrong">
        <title>%s</title>
    </head>
    """ % title


def print_doctype():
    """Print the html5 doctype"""
    print "<!DOCTYPE html>"


def print_html_start_tag():
    """Print the html opening tag"""
    print "<html>"


def print_html_end_tag():
    """Print the html closing tag"""
    print "</html>"


def print_page_header():
    """Print the header"""
    print """
    <header>
        <h1>Steam Game Backlog</h1>
    </header>
    """


def print_body_start_tag():
    """The pages Body start tag"""
    print "<body>"


def print_body_end_tag():
    """The pages body end tag"""
    print "</body>"


def print_nav():
    """Print the websites nav section"""
    print """
    <nav>
        <ul>
            <li><a href="index.py">Home</a></li>
            <li><a href="index.py">Home</a></li>
            <li><a href="index.py">Home</a></li>
            <li><a href="index.py">Home</a></li>
            <li><a href="index.py">Home</a></li>
        </ul>
    </nav>
    """


def setup_page(head_title="Steam Game Backlog"):
    """Setup the start of the html page
    :param head_title: The title to be displayed in the title bar or tab of the browser
    """
    print_cgi_header()
    print_doctype()
    print_html_start_tag()
    print_head(head_title)
    print_body_start_tag()
    print_page_header()
    print_nav()


def close_page_tags():
    """Close off the tags from the page setup"""
    print_body_end_tag()
    print_html_end_tag()
