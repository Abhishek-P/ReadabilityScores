# [readability - scores](http://readability-scores.herokuapp.com)
__readability-scores__ is a simple flask service built to provide text statistics 
and readability scores for use with [__ReaSE__](https://github.com/Abhishek-P/ReaSE).

This is built with simple /get and /set.

Text has to be sent as arg 'text' in a POST request.
Text statistics will be made available at  /get/stats as json dictionary.

####Step 1:
/set : text= < text > POST request Args not form
####Step 2:
/get/stats :  returns JSON of stats

/get/< stat-name > : returns value of the specific stat

####Stats available:
*  letter_count
*   word_count
*   syllable_count
*   sentence_count
*   complex_words
*   fk_index
*   gf_index
*   cl_index
*   dc_index
*   as_index

Requires:

*   Flask
*   NLTK - tokenize

Enjoy.
Please ping me at  [abhijnvb@gmail.com](mailto:abhijnvb@gmail.com) for further info.


  