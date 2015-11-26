#!/usr/bin/env python


def print_cgi_header():
    """Print out the required CGI header"""
    print("Content-Type: text/html")
    print("")


def print_head(title=""):
    """Print the standard page head
    :param title: The title to be displayed in the title bar or tab of the browser
    """
    print """
        <HEAD>
        <TITLE>%s</TITLE>
        </HEAD>
        """ % title


def print_html_start_tag():
    """Print the html opening tag"""
    print "<HTML>"


def print_html_end_tag():
    """Print the html closing tag"""
    print "</HTML>"
