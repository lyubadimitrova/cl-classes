==============================================================
Spanish corpus for the CoNLL-2009 shared task
"Syntactic and Semantic Dependencies in Multiple Languages"
Version 1.1: January 9, 2009
==============================================================

This file contains the basic information regarding the Spanish corpus
provided for the CoNLL-2009 shared task on "Syntactic and Semantic
Dependencies in Multiple Languages". The current version (1.1, January
9, 2009) corresponds to the release of the trial data sets. The
complete materials will be made available by January 19, 2009. All
changes and updates on these data sets are reported in Section 1 of
this document.

(1) LIST OF VERSIONS

  1.1 (2009-01-09): several updates have been made: 
    - Erroneous '\t' characters have been eliminated from the trial
      data set "CoNLL2009-ST-Spanish-trial.txt"
    - The description of the verbal lexicon has been extended in the
      README.txt file (section 2), including details on the difference
      between
    - Verbal lexicon files have been corrected in order to convert LSS
      tags into the format described in the tagset document
      "tagsets.pdf" (e.g., "1.1" => "a1", "2.2" => "b2", etc.)

  1.0 (1009-01-05): initial distribution of the Trial data sets


(2) CONTENTS OF THE DISTRIBUTION 1.1

We are providing the following documents:

* README.txt 
  this file

* CoNLL2009-ST-Spanish-trial.txt
  the trial data set for Spanish (50 sample sentences)

* tagsets.pdf 
  PDF document describing the tagsets of all levels of linguistic
  annotation: PoS tags and additional features, syntactic dependencies
  (syntactic functions), semantic dependencies (arguments and thematic
  roles) and predicate semantic classes (Lexical Semantic
  Structure, LSS). Tag sets are shared by the two languages.

* verbal-lexicon.es.tgz
  Tarball containing the Spanish verbal lexicon. This lexicon
  contains, for each verbal predicate in the corpus, the mapping from
  syntactic functions to thematic roles and the corresponding semantic
  class (LSS, ELS in Spanish). In the lexicon, each verbal predicate
  may be divided into different numbered senses (01, 02, 03, ...),
  where each sense is related to one or more semantic classes,
  basically differentiated according to the four event classes
  -accomplishments (a), achievements (b), states (c) and activities
  (d)-, and on the diatheses alternations in which a sense can
  occur. The "EXAMPLE.pdf" file included in the tarball shows an
  example of a verbal entry in the lexicon.
  More information on the verbal lexicons can be obtained at
  the ANCORA website: http://clic.ub.edu/ancora  


(3) ON THE CATALAN AND SPANISH DATA SETS

The Catalan and Spanish corpora for the CoNLL-2009 shared task are
compliant with the standard formatting described in the shared task
web site (http://ufal.mff.cuni.cz/conll2009-st/). The sizes of the
corpora will be:

   Catalan: 496,672 lexical tokens
      training: 390,302 
      development: 53,015
      test: 53,355

   Spanish: 528,440 lexical tokens
      training: 427,442 
      development: 50,368
      test: 50,630

The special features of these corpora are: 

* Dependency trees are projective
* Only verbal predicates are annotated (with exceptional cases
  referring to words that can be adjectives and past_participles, 
  see the document on tagsets)
* No word can be the argument of more than one predicate in a sentence
* Semantic dependency labels are composed by a numeric argument plus a
  thematic role label (see tagsets.pdf for details)
* Predicate senses correspond to a Lexical Sematic Structure label
  (see tagsets.pdf for details)
* The corpus is segmented so multi-words, named entities, temporal
  expressions, compounds, etc. are grouped together
* Segmentation also accounts for elliptical pronouns (there are marked
  as empty lexical tokens "_" with a pronoun POS tag)

The following tools have been used to generate the Predicted (P-) columns:

* PLEMMA, PPOS, PFEAT are generated with the FreeLing Open source
  suite of Language Analyzers (http://www.lsi.upc.es/~nlp/freeling/)
  Thanks to Lluís Padró (UPC) for helping with the annotation of the
  morphosyntactic information.

* PHEAD and PDEPREL are generated using MaltParser
  (http://w3.msi.vxu.se/~jha/maltparser/) and JointParser
  (http://www.lsi.upc.edu/~xlluis/jointparser/). Thanks to Xavier
  Lluís (UPC) for helping with the annotation of this part.

Sources of the Catalan and Spanish data sets:

  The Catalan and Spanish data sets are extracted from the Ancora
  corpora (see http://clic.ub.edu/ancora). AnCora-ES (the Spanish
  part) contains 75,000 words from the Lexesp Spanish balanced
  6-million-word corpus, 225,000 words from the EFE Spanish news
  agency, and 200,000 from the Spanish version of the `El Periódico'
  newspaper. AnCora-CA (the Catalan part) consists of 75,000 words
  from the EFE news agency, 225,000 words from the ACN Catalan news
  agency, and 200,000 words from the Catalan version of the `El
  Periódico´ newspaper. The subset of 200,000 words coming from El
  Periódico corresponds to the same news in Catalan and Spanish,
  spanning from January to December 2000.


(4) ORGANIZATION

  Lluís Màrquez 
  Universitat Politècnica de Catalunya (UPC), Barcelona, Spain 
  lluism@lsi.upc.edu
  http://www.lsi.upc.edu/~lluism

  Ma. Antònia Martí, 
  Universitat de Barcelona (UB), Barcelona, Spain
  amarti@ub.edu
  http://clic.ub.edu

  Other people behind the preparation of the corpora:

  Mariona Taulé, CLiC, UB 
  Manuel Bertran, CLiC, UB
  Oriol Borrega, CLiC, UB

