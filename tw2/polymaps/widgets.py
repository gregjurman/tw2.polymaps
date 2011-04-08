"""
TODO
"""

import tw2.core as twc
from tw2.core.resources import encoder
import resources as res
import simplejson

class PolyMap(twc.Widget):
    template = "mako:tw2.polymaps.templates.polymap"
    resources = [res.pm_js, res.custom_js]

    data_url = twc.Param("""Url to pull a geoJSON layer from""", default=None)

    arrow = twc.Param(
        """Constructs an arrow control with default settings. The arrow control
        provides key listeners for the arrow keys for panning, and the plus and
        minus keys for zooming. The arrow control allows multiple keys to be
        pressed simultaneously; for example, the pressing the left and down
        arrows simultaneously will cause the map to pan diagonally.   (bool)""",
        default=False)

    compass = twc.Param(
        """    Constructs a compass control with default settings. The compass
        control provides a user interface widget for panning and zooming as an
        alternative to mouse and keyboard controls. The compass also provides
        shift-drag support for zooming to a given extent.

            The compass is not part of the standard set of interaction controls
        (see interact). The compass control is rendered using SVG elements
        and must be styled through CSS. An example stylesheet is available in
        the Git repository.  (bool)""",
        default=False)

    dblclick = twc.Param(
        """Constructs a double-click control with default settings. This control
        allows the user to double-click to zoom in on the given point, and
        shift-double-click to zoom out. The double-click snaps to the nearest
        integral zoom level, providing optimal display of tiles.   (bool)""",
        default=False)

    drag = twc.Param(
        """Constructs a drag control with default settings. The drag control
        allows the user to pan the map with the mouse by clicking and dragging.
        (bool)""", default=False)

    grid = twc.Param(
        """    Constructs a grid control with default settings. The grid control
        provides reference lines of constant longitude and latitude that are
        overlaid on the map. The resolution of the reference lines increases
        with zoom level.

            The grid is not part of the standard set of interaction controls
        (see po.interact). The grid control is rendered using SVG elements and
        must be styled through CSS. An example stylesheet is available in the
        Git repository.  (bool)""",
        default=False)

    hash = twc.Param(
        """    Constructs a hash control with default settings. The hash control
        provides two-way coordination of the window's location hash with the map
        center and zoom. This allows map URLs to be conveniently
        copy-and-pasted, preserving the view. To further cut down on URL length,
        the precision of latitude and longitude is based on the zoom level.

            The hash control also listens for the window hashchange event,
        such that links on the page or editing via the address bar can update
        the map center and zoom.  (bool)""",
        default=False)

    interact = twc.Param(
        """ Constructs the standard interaction controls with default settings.
        This includes the drag, wheel, dblclick and arrow controls. This control
        set does not allow customization; to customize controls, add them
        individually instead.   (bool)""",
        default=False)

    wheel = twc.Param(
        """ Constructs a mouse wheel control with default settings. This control
        uses the mousewheel event to provide smooth zooming around the mouse
        cursor, and is designed to support both discrete devices (such as the
        traditional mouse wheel) and continuous devices (such as trackpads).
        (bool)""", default=False)




    def js_arguments(self):
        json = simplejson.dumps(
            [
                self.attrs, self.data_url,
                self.arrow, self.compass, self.dblclick, self.drag,
                self.grid, self.hash, self.interact, self.wheel,
            ])
        json = json[1:-1]
        print json
        return json
