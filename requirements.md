Improve the Python quality of nyancat.py by factoring magic numbers and string literals out into named constants. This covers ANSI escape sequences, timing values, and numeric literals used in the rainbow and viewport calculations.

Add support for selectable colour schemes via a --scheme CLI argument. Schemes are defined in schemes.py as ColourScheme TypedDicts, each specifying a colours dict and a rainbow string. Each flag scheme applies that flag's colours to both the rainbow trail and the poptart stripes. A --random flag (mutually exclusive with --scheme) selects a scheme at random.

When neither flag is given, the scheme auto-selects by date: pinks on March 8 (International Women's Day), ireland on March 17 (St. Patrick's Day), italy on June 2 (Festa della Repubblica), india on August 15 (Independence Day), sealand on September 2 (founding date), cyprus on October 1, germany on October 3 (Tag der Deutschen Einheit), spain on October 12 (Fiesta Nacional), poland on November 11 (Święto Niepodległości), greece on March 25 (Greek Independence Day), trans throughout June (pride month), and rainbow otherwise.

Add a rs preview command that launches each scheme in an xterm, screenshots it with ImageMagick import, and assembles the results into a labelled grid PNG using montage. The scheme list is read dynamically from schemes.py so new schemes appear automatically.

Add a rs record command that launches nyancat in an xterm, captures frames using ImageMagick import at 12fps, and assembles them into an optimised GIF using ffmpeg's palette filter. Output defaults to nyan.gif in the project root. Scheme and duration are configurable as positional arguments.
