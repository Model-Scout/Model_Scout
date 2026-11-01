# Unicode 10.0 Character Database in JSON

Machine-readable information on Unicode 10.0 Characters

### Context: 

In working on Unicode implementations, it is often useful to access the full content of the Unicode Character Database (UCD). For example, in establishing mappings from characters to glyphs in fonts, it is convenient to see the character scalar value, the character name, the character East Asian width, along with the shape and metrics of the proposed glyph to map to; looking at all this data simultaneously helps in evaluating the mapping.

This is a machine-readable version of the Unicode Character Database in JSON format.

### Content:

The majority of information about individual codepoints is represented using properties. Each property, except for the Special_Case_Condition and Name_Alias properties, is represented by an attribute. In an XML data file, the absence of an attribute (may be only on some code-points) means that the document does not express the value of the corresponding property. Conversely, the presence of an attribute is an expression of the corresponding property value; the implied null value is represented by the empty string.
 
The Name_Alias property is represented by zero or more name-alias child elements. Unlike the situation for properties represented by attributes, it is not possible to determine whether all of the aliases have been represented in a data file by inspecting that data file.
 
The name of an attribute is the abbreviated name of the property as given in the file PropertyAliases.txt in version 6.1.0 of the UCD. For the Unihan properties, the name is that given in the various versions of the Unihan database (some properties are no longer present in version 6.1.0).
 
For catalog and enumerated properties, the values are those listed in the file PropertyValueAliases.txt in version 6.1.0 of the UCD; if there is an abbreviated name, it is used, otherwise the long name is used.
Note that the set of possible values for a property captured in this schema may change from one version to the next.

The following properties are associated with code points:

*     Age property
*     Name properties
*     Name Aliases
*     Block
*     General Category
*     Combining properties
*     Bidirectionality properties
*     Decomposition properties
*     Numeric Properties
*     Joining properties
*     Linebreak properties
*     East Asian Width property
*     Case properties
*     Script properties
*     ISO Comment properties
*     Hangul properties
*     Indic properties
*     Identifier and Pattern and programming language properties
*     Properties related to function and graphic characteristics
*     Properties related to boundaries
*     Properties related to ideographs
*     Miscellaneous properties
*     Unihan properties
*     Tangut data
*     Nushu data

For additional information, [please consult the full documentation on the Unicode website](https://www.unicode.org/reports/tr42/).

### Acknowledgements: 

Copyright © 1991-2017 Unicode, Inc. All rights reserved. Distributed under the Terms of Use in http://www.unicode.org/copyright.html.

Permission is hereby granted, free of charge, to any person obtaining a copy of the Unicode data files and any associated documentation (the "Data Files") or Unicode software and any associated documentation
(the "Software") to deal in the Data Files or Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, and/or sell copies of the Data Files or Software, and to permit persons to whom the Data Files or Software are furnished to do so, provided that either
(a) this copyright and permission notice appear with all copies of the Data Files or Software, or
(b) this copyright and permission notice appear in associated Documentation.

출처: Kaggle (rtatman/unicode-100-character-database-in-json)
태그: languages, real estate, linguistics, computer science, programming, software
라이선스: Data files © Original Authors
수정일: 2017-12-15T19:21:54.423Z
