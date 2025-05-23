from django import template

register = template.Library()

@register.simple_tag
def get_links():
    links =  [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    }, {
        'name': 'Marketplace',
        'href': '/marketplace/',
        'icon': 'fa-newspaper',
    },{
        'name': 'News',
        'href': '/news',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
    }, {
        'name':'Terms of Service',
        'href': '/terms-of-service',
        'icon': 'fa-solid fa-bars'
    }]

    return links

@register.simple_tag
def get_links_authenticated():
    links =  [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    },{
        'name': 'Marketplace',
        'href': '/marketplace/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Add post',
        'href': '/marketplace/create',
        'icon': 'fa-plus',
    },{
        'name': 'News',
        'href': '/news',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
    }, {
        'name':'Terms of Service',
        'href': '/terms-of-service',
        'icon': 'fa-solid fa-bars'
    }]
         
    return links
