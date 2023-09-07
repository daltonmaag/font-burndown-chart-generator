"""
This type stub file was generated by pyright.
"""

from matplotlib import _api
from matplotlib.path import Path

_log = ...
class TextToPath:
    """A class that converts strings to paths."""
    FONT_SCALE = ...
    DPI = ...
    def __init__(self) -> None:
        ...
    
    def get_text_width_height_descent(self, s, prop, ismath): # -> tuple[Literal[0], Literal[0], Literal[0]] | tuple[Unknown, Unknown, Unknown]:
        ...
    
    def get_text_path(self, prop, s, ismath=...): # -> tuple[NDArray[float64] | list[Unknown], list[Unknown]]:
        """
        Convert text *s* to path (a tuple of vertices and codes for
        matplotlib.path.Path).

        Parameters
        ----------
        prop : `~matplotlib.font_manager.FontProperties`
            The font properties for the text.

        s : str
            The text to be converted.

        ismath : {False, True, "TeX"}
            If True, use mathtext parser.  If "TeX", use tex for rendering.

        Returns
        -------
        verts : list
            A list of numpy arrays containing the x and y coordinates of the
            vertices.

        codes : list
            A list of path codes.

        Examples
        --------
        Create a list of vertices and codes from a text, and create a `.Path`
        from those::

            from matplotlib.path import Path
            from matplotlib.text import TextToPath
            from matplotlib.font_manager import FontProperties

            fp = FontProperties(family="Humor Sans", style="italic")
            verts, codes = TextToPath().get_text_path(fp, "ABC")
            path = Path(verts, codes, closed=False)

        Also see `TextPath` for a more direct way to create a path from a text.
        """
        ...
    
    def get_glyphs_with_font(self, font, s, glyph_map=..., return_new_glyphs_only=...): # -> tuple[list[tuple[Unknown, Unknown, int, float]], OrderedDict[Unknown, Unknown] | Unknown, list[Unknown]]:
        """
        Convert string *s* to vertices and codes using the provided ttf font.
        """
        ...
    
    def get_glyphs_mathtext(self, prop, s, glyph_map=..., return_new_glyphs_only=...): # -> tuple[list[tuple[Unknown, Unknown, Unknown, Unknown]], OrderedDict[Unknown, Unknown] | Unknown, list[Unknown]]:
        """
        Parse mathtext string *s* and convert it to a (vertices, codes) pair.
        """
        ...
    
    @_api.deprecated("3.6", alternative="TexManager()")
    def get_texmanager(self): # -> TexManager:
        """Return the cached `~.texmanager.TexManager` instance."""
        ...
    
    def get_glyphs_tex(self, prop, s, glyph_map=..., return_new_glyphs_only=...): # -> tuple[list[tuple[Unknown, Unknown, Unknown, Unknown]], OrderedDict[Unknown, Unknown] | Unknown, list[Unknown]]:
        """Convert the string *s* to vertices and codes using usetex mode."""
        ...
    


text_to_path = ...
class TextPath(Path):
    """
    Create a path from the text.
    """
    def __init__(self, xy, s, size=..., prop=..., _interpolation_steps=..., usetex=...) -> None:
        r"""
        Create a path from the text. Note that it simply is a path,
        not an artist. You need to use the `.PathPatch` (or other artists)
        to draw this path onto the canvas.

        Parameters
        ----------
        xy : tuple or array of two float values
            Position of the text. For no offset, use ``xy=(0, 0)``.

        s : str
            The text to convert to a path.

        size : float, optional
            Font size in points. Defaults to the size specified via the font
            properties *prop*.

        prop : `~matplotlib.font_manager.FontProperties`, optional
            Font property. If not provided, will use a default
            `.FontProperties` with parameters from the
            :ref:`rcParams<customizing-with-dynamic-rc-settings>`.

        _interpolation_steps : int, optional
            (Currently ignored)

        usetex : bool, default: False
            Whether to use tex rendering.

        Examples
        --------
        The following creates a path from the string "ABC" with Helvetica
        font face; and another path from the latex fraction 1/2::

            from matplotlib.text import TextPath
            from matplotlib.font_manager import FontProperties

            fp = FontProperties(family="Helvetica", style="italic")
            path1 = TextPath((12, 12), "ABC", size=12, prop=fp)
            path2 = TextPath((0, 0), r"$\frac{1}{2}$", size=12, usetex=True)

        Also see :doc:`/gallery/text_labels_and_annotations/demo_text_path`.
        """
        ...
    
    def set_size(self, size): # -> None:
        """Set the text size."""
        ...
    
    def get_size(self):
        """Get the text size."""
        ...
    
    @property
    def vertices(self): # -> None:
        """
        Return the cached path after updating it if necessary.
        """
        ...
    
    @property
    def codes(self): # -> NDArray[code_type] | None:
        """
        Return the codes
        """
        ...
    


