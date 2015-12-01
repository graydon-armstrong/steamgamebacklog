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

def print_header():
    """Print the header"""
    print'<h1>Steam Game Backlog</h1>'


def setup_page(head_title="Steam Game Backlog"):
    """Setup the start of the html page"""
    print_cgi_header()
    print_doctype()
    print_html_start_tag()
    print_head(head_title)
    print_header()
