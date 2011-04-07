
import tw2.core as twc
from tw2.polymaps.defaults import __basename__, __version__
modname = ".".join(__name__.split('.')[:-1])


pm_js = twc.JSLink(
    modname=modname, filename='static/%s/%s/polymaps.min.js' % (
        __basename__, __version__))

custom_js = twc.JSLink(
    modname=modname, filename='static/custom/js/tw2.polymaps.js')

custom_css = twc.CSSLink(
    modname=modname, filename='static/custom/css/tw2.polymaps.css')
