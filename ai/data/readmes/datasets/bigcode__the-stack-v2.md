---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
language:
- code
license:
- other
multilinguality:
- multilingual
pretty_name: The-Stack-v2
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids: []

extra_gated_prompt: |-
  ## Terms of Use for The Stack v2

  The Stack v2 dataset is a collection of source code in over 600 programming languages. We ask that you read and acknowledge the following points before using the dataset:
  1. Downloading the dataset in bulk requires a an agreement with SoftwareHeritage and INRIA. Contact [datasets@softwareheritage.org](mailto:datasets@softwareheritage.org?subject=TheStackV2%20request%20for%20dataset%20access%20information) for more information.
  2. If you are using the dataset to train models you must adhere to the SoftwareHeritage [principles for language model training](https://www.softwareheritage.org/2023/10/19/swh-statement-on-llm-for-code/).
  3. The Stack v2 is a collection of source code from repositories with various licenses. Any use of all or part of the code gathered in The Stack v2 must abide by the terms of the original licenses, including attribution clauses when relevant. We facilitate this by providing provenance information for each data point.
  4. The Stack v2 is regularly updated to enact validated data removal requests. By clicking on "Access repository", you agree to update your own version of The Stack v2 to the most recent usable version.

  By clicking on "Access repository" below, you accept that your contact information (email address and username) can be shared with the dataset maintainers as well.
    
extra_gated_fields:
 Email: text
 I have read the License and agree with its terms: checkbox
dataset_info:
  features:
  - name: blob_id
    dtype: string
  - name: directory_id
    dtype: string
  - name: path
    dtype: string
  - name: content_id
    dtype: string
  - name: detected_licenses
    sequence: string
  - name: license_type
    dtype: string
  - name: repo_name
    dtype: string
  - name: snapshot_id
    dtype: string
  - name: revision_id
    dtype: string
  - name: branch_name
    dtype: string
  - name: visit_date
    dtype: timestamp[ns]
  - name: revision_date
    dtype: timestamp[ns]
  - name: committer_date
    dtype: timestamp[ns]
  - name: github_id
    dtype: int64
  - name: star_events_count
    dtype: int64
  - name: fork_events_count
    dtype: int64
  - name: gha_license_id
    dtype: string
  - name: gha_event_created_at
    dtype: timestamp[ns]
  - name: gha_created_at
    dtype: timestamp[ns]
  - name: gha_language
    dtype: string
  - name: src_encoding
    dtype: string
  - name: language
    dtype: string
  - name: is_vendor
    dtype: bool
  - name: is_generated
    dtype: bool
  - name: length_bytes
    dtype: int64
  - name: extension
    dtype: string
configs:
  - config_name: default
    default: true
    data_files:
      - split: train
        path: "data/*/*.parquet"
  - config_name: "1C_Enterprise"
    data_files:
      - split: train
        path: "data/1C_Enterprise/*.parquet"
  - config_name: "2-Dimensional_Array"
    data_files:
      - split: train
        path: "data/2-Dimensional_Array/*.parquet"
  - config_name: "4D"
    data_files:
      - split: train
        path: "data/4D/*.parquet"
  - config_name: "ABAP"
    data_files:
      - split: train
        path: "data/ABAP/*.parquet"
  - config_name: "ABAP_CDS"
    data_files:
      - split: train
        path: "data/ABAP_CDS/*.parquet"
  - config_name: "ABNF"
    data_files:
      - split: train
        path: "data/ABNF/*.parquet"
  - config_name: "AGS_Script"
    data_files:
      - split: train
        path: "data/AGS_Script/*.parquet"
  - config_name: "AIDL"
    data_files:
      - split: train
        path: "data/AIDL/*.parquet"
  - config_name: "AL"
    data_files:
      - split: train
        path: "data/AL/*.parquet"
  - config_name: "AMPL"
    data_files:
      - split: train
        path: "data/AMPL/*.parquet"
  - config_name: "ANTLR"
    data_files:
      - split: train
        path: "data/ANTLR/*.parquet"
  - config_name: "API_Blueprint"
    data_files:
      - split: train
        path: "data/API_Blueprint/*.parquet"
  - config_name: "APL"
    data_files:
      - split: train
        path: "data/APL/*.parquet"
  - config_name: "ASL"
    data_files:
      - split: train
        path: "data/ASL/*.parquet"
  - config_name: "ASN.1"
    data_files:
      - split: train
        path: "data/ASN.1/*.parquet"
  - config_name: "ASP.NET"
    data_files:
      - split: train
        path: "data/ASP.NET/*.parquet"
  - config_name: "ATS"
    data_files:
      - split: train
        path: "data/ATS/*.parquet"
  - config_name: "ActionScript"
    data_files:
      - split: train
        path: "data/ActionScript/*.parquet"
  - config_name: "Ada"
    data_files:
      - split: train
        path: "data/Ada/*.parquet"
  - config_name: "Adobe_Font_Metrics"
    data_files:
      - split: train
        path: "data/Adobe_Font_Metrics/*.parquet"
  - config_name: "Agda"
    data_files:
      - split: train
        path: "data/Agda/*.parquet"
  - config_name: "Alloy"
    data_files:
      - split: train
        path: "data/Alloy/*.parquet"
  - config_name: "Alpine_Abuild"
    data_files:
      - split: train
        path: "data/Alpine_Abuild/*.parquet"
  - config_name: "Altium_Designer"
    data_files:
      - split: train
        path: "data/Altium_Designer/*.parquet"
  - config_name: "AngelScript"
    data_files:
      - split: train
        path: "data/AngelScript/*.parquet"
  - config_name: "Ant_Build_System"
    data_files:
      - split: train
        path: "data/Ant_Build_System/*.parquet"
  - config_name: "Antlers"
    data_files:
      - split: train
        path: "data/Antlers/*.parquet"
  - config_name: "ApacheConf"
    data_files:
      - split: train
        path: "data/ApacheConf/*.parquet"
  - config_name: "Apex"
    data_files:
      - split: train
        path: "data/Apex/*.parquet"
  - config_name: "Apollo_Guidance_Computer"
    data_files:
      - split: train
        path: "data/Apollo_Guidance_Computer/*.parquet"
  - config_name: "AppleScript"
    data_files:
      - split: train
        path: "data/AppleScript/*.parquet"
  - config_name: "Arc"
    data_files:
      - split: train
        path: "data/Arc/*.parquet"
  - config_name: "AsciiDoc"
    data_files:
      - split: train
        path: "data/AsciiDoc/*.parquet"
  - config_name: "AspectJ"
    data_files:
      - split: train
        path: "data/AspectJ/*.parquet"
  - config_name: "Assembly"
    data_files:
      - split: train
        path: "data/Assembly/*.parquet"
  - config_name: "Astro"
    data_files:
      - split: train
        path: "data/Astro/*.parquet"
  - config_name: "Asymptote"
    data_files:
      - split: train
        path: "data/Asymptote/*.parquet"
  - config_name: "Augeas"
    data_files:
      - split: train
        path: "data/Augeas/*.parquet"
  - config_name: "AutoHotkey"
    data_files:
      - split: train
        path: "data/AutoHotkey/*.parquet"
  - config_name: "AutoIt"
    data_files:
      - split: train
        path: "data/AutoIt/*.parquet"
  - config_name: "Avro_IDL"
    data_files:
      - split: train
        path: "data/Avro_IDL/*.parquet"
  - config_name: "Awk"
    data_files:
      - split: train
        path: "data/Awk/*.parquet"
  - config_name: "BASIC"
    data_files:
      - split: train
        path: "data/BASIC/*.parquet"
  - config_name: "Ballerina"
    data_files:
      - split: train
        path: "data/Ballerina/*.parquet"
  - config_name: "Batchfile"
    data_files:
      - split: train
        path: "data/Batchfile/*.parquet"
  - config_name: "Beef"
    data_files:
      - split: train
        path: "data/Beef/*.parquet"
  - config_name: "Befunge"
    data_files:
      - split: train
        path: "data/Befunge/*.parquet"
  - config_name: "Berry"
    data_files:
      - split: train
        path: "data/Berry/*.parquet"
  - config_name: "BibTeX"
    data_files:
      - split: train
        path: "data/BibTeX/*.parquet"
  - config_name: "Bicep"
    data_files:
      - split: train
        path: "data/Bicep/*.parquet"
  - config_name: "Bikeshed"
    data_files:
      - split: train
        path: "data/Bikeshed/*.parquet"
  - config_name: "Bison"
    data_files:
      - split: train
        path: "data/Bison/*.parquet"
  - config_name: "BitBake"
    data_files:
      - split: train
        path: "data/BitBake/*.parquet"
  - config_name: "Blade"
    data_files:
      - split: train
        path: "data/Blade/*.parquet"
  - config_name: "BlitzBasic"
    data_files:
      - split: train
        path: "data/BlitzBasic/*.parquet"
  - config_name: "BlitzMax"
    data_files:
      - split: train
        path: "data/BlitzMax/*.parquet"
  - config_name: "Bluespec"
    data_files:
      - split: train
        path: "data/Bluespec/*.parquet"
  - config_name: "Boo"
    data_files:
      - split: train
        path: "data/Boo/*.parquet"
  - config_name: "Boogie"
    data_files:
      - split: train
        path: "data/Boogie/*.parquet"
  - config_name: "Brainfuck"
    data_files:
      - split: train
        path: "data/Brainfuck/*.parquet"
  - config_name: "BrighterScript"
    data_files:
      - split: train
        path: "data/BrighterScript/*.parquet"
  - config_name: "Brightscript"
    data_files:
      - split: train
        path: "data/Brightscript/*.parquet"
  - config_name: "Browserslist"
    data_files:
      - split: train
        path: "data/Browserslist/*.parquet"
  - config_name: "C"
    data_files:
      - split: train
        path: "data/C/*.parquet"
  - config_name: "C++"
    data_files:
      - split: train
        path: "data/C++/*.parquet"
  - config_name: "C-ObjDump"
    data_files:
      - split: train
        path: "data/C-ObjDump/*.parquet"
  - config_name: "C-Sharp"
    data_files:
      - split: train
        path: "data/C-Sharp/*.parquet"
  - config_name: "C2hs_Haskell"
    data_files:
      - split: train
        path: "data/C2hs_Haskell/*.parquet"
  - config_name: "CAP_CDS"
    data_files:
      - split: train
        path: "data/CAP_CDS/*.parquet"
  - config_name: "CIL"
    data_files:
      - split: train
        path: "data/CIL/*.parquet"
  - config_name: "CLIPS"
    data_files:
      - split: train
        path: "data/CLIPS/*.parquet"
  - config_name: "CMake"
    data_files:
      - split: train
        path: "data/CMake/*.parquet"
  - config_name: "COBOL"
    data_files:
      - split: train
        path: "data/COBOL/*.parquet"
  - config_name: "CODEOWNERS"
    data_files:
      - split: train
        path: "data/CODEOWNERS/*.parquet"
  - config_name: "COLLADA"
    data_files:
      - split: train
        path: "data/COLLADA/*.parquet"
  - config_name: "CSON"
    data_files:
      - split: train
        path: "data/CSON/*.parquet"
  - config_name: "CSS"
    data_files:
      - split: train
        path: "data/CSS/*.parquet"
  - config_name: "CSV"
    data_files:
      - split: train
        path: "data/CSV/*.parquet"
  - config_name: "CUE"
    data_files:
      - split: train
        path: "data/CUE/*.parquet"
  - config_name: "CWeb"
    data_files:
      - split: train
        path: "data/CWeb/*.parquet"
  - config_name: "Cabal_Config"
    data_files:
      - split: train
        path: "data/Cabal_Config/*.parquet"
  - config_name: "Cadence"
    data_files:
      - split: train
        path: "data/Cadence/*.parquet"
  - config_name: "Cairo"
    data_files:
      - split: train
        path: "data/Cairo/*.parquet"
  - config_name: "CameLIGO"
    data_files:
      - split: train
        path: "data/CameLIGO/*.parquet"
  - config_name: "Cap-n_Proto"
    data_files:
      - split: train
        path: "data/Cap-n_Proto/*.parquet"
  - config_name: "CartoCSS"
    data_files:
      - split: train
        path: "data/CartoCSS/*.parquet"
  - config_name: "Ceylon"
    data_files:
      - split: train
        path: "data/Ceylon/*.parquet"
  - config_name: "Chapel"
    data_files:
      - split: train
        path: "data/Chapel/*.parquet"
  - config_name: "Charity"
    data_files:
      - split: train
        path: "data/Charity/*.parquet"
  - config_name: "Checksums"
    data_files:
      - split: train
        path: "data/Checksums/*.parquet"
  - config_name: "ChucK"
    data_files:
      - split: train
        path: "data/ChucK/*.parquet"
  - config_name: "Cirru"
    data_files:
      - split: train
        path: "data/Cirru/*.parquet"
  - config_name: "Clarion"
    data_files:
      - split: train
        path: "data/Clarion/*.parquet"
  - config_name: "Clarity"
    data_files:
      - split: train
        path: "data/Clarity/*.parquet"
  - config_name: "Classic_ASP"
    data_files:
      - split: train
        path: "data/Classic_ASP/*.parquet"
  - config_name: "Clean"
    data_files:
      - split: train
        path: "data/Clean/*.parquet"
  - config_name: "Click"
    data_files:
      - split: train
        path: "data/Click/*.parquet"
  - config_name: "Clojure"
    data_files:
      - split: train
        path: "data/Clojure/*.parquet"
  - config_name: "Closure_Templates"
    data_files:
      - split: train
        path: "data/Closure_Templates/*.parquet"
  - config_name: "Cloud_Firestore_Security_Rules"
    data_files:
      - split: train
        path: "data/Cloud_Firestore_Security_Rules/*.parquet"
  - config_name: "CoNLL-U"
    data_files:
      - split: train
        path: "data/CoNLL-U/*.parquet"
  - config_name: "CodeQL"
    data_files:
      - split: train
        path: "data/CodeQL/*.parquet"
  - config_name: "CoffeeScript"
    data_files:
      - split: train
        path: "data/CoffeeScript/*.parquet"
  - config_name: "ColdFusion"
    data_files:
      - split: train
        path: "data/ColdFusion/*.parquet"
  - config_name: "ColdFusion_CFC"
    data_files:
      - split: train
        path: "data/ColdFusion_CFC/*.parquet"
  - config_name: "Common_Lisp"
    data_files:
      - split: train
        path: "data/Common_Lisp/*.parquet"
  - config_name: "Common_Workflow_Language"
    data_files:
      - split: train
        path: "data/Common_Workflow_Language/*.parquet"
  - config_name: "Component_Pascal"
    data_files:
      - split: train
        path: "data/Component_Pascal/*.parquet"
  - config_name: "Cool"
    data_files:
      - split: train
        path: "data/Cool/*.parquet"
  - config_name: "Coq"
    data_files:
      - split: train
        path: "data/Coq/*.parquet"
  - config_name: "Creole"
    data_files:
      - split: train
        path: "data/Creole/*.parquet"
  - config_name: "Crystal"
    data_files:
      - split: train
        path: "data/Crystal/*.parquet"
  - config_name: "Csound"
    data_files:
      - split: train
        path: "data/Csound/*.parquet"
  - config_name: "Csound_Document"
    data_files:
      - split: train
        path: "data/Csound_Document/*.parquet"
  - config_name: "Csound_Score"
    data_files:
      - split: train
        path: "data/Csound_Score/*.parquet"
  - config_name: "Cuda"
    data_files:
      - split: train
        path: "data/Cuda/*.parquet"
  - config_name: "Cue_Sheet"
    data_files:
      - split: train
        path: "data/Cue_Sheet/*.parquet"
  - config_name: "Curry"
    data_files:
      - split: train
        path: "data/Curry/*.parquet"
  - config_name: "Cycript"
    data_files:
      - split: train
        path: "data/Cycript/*.parquet"
  - config_name: "Cython"
    data_files:
      - split: train
        path: "data/Cython/*.parquet"
  - config_name: "D"
    data_files:
      - split: train
        path: "data/D/*.parquet"
  - config_name: "DIGITAL_Command_Language"
    data_files:
      - split: train
        path: "data/DIGITAL_Command_Language/*.parquet"
  - config_name: "DM"
    data_files:
      - split: train
        path: "data/DM/*.parquet"
  - config_name: "DNS_Zone"
    data_files:
      - split: train
        path: "data/DNS_Zone/*.parquet"
  - config_name: "DTrace"
    data_files:
      - split: train
        path: "data/DTrace/*.parquet"
  - config_name: "Dafny"
    data_files:
      - split: train
        path: "data/Dafny/*.parquet"
  - config_name: "Darcs_Patch"
    data_files:
      - split: train
        path: "data/Darcs_Patch/*.parquet"
  - config_name: "Dart"
    data_files:
      - split: train
        path: "data/Dart/*.parquet"
  - config_name: "DataWeave"
    data_files:
      - split: train
        path: "data/DataWeave/*.parquet"
  - config_name: "Debian_Package_Control_File"
    data_files:
      - split: train
        path: "data/Debian_Package_Control_File/*.parquet"
  - config_name: "DenizenScript"
    data_files:
      - split: train
        path: "data/DenizenScript/*.parquet"
  - config_name: "Dhall"
    data_files:
      - split: train
        path: "data/Dhall/*.parquet"
  - config_name: "Diff"
    data_files:
      - split: train
        path: "data/Diff/*.parquet"
  - config_name: "DirectX_3D_File"
    data_files:
      - split: train
        path: "data/DirectX_3D_File/*.parquet"
  - config_name: "Dockerfile"
    data_files:
      - split: train
        path: "data/Dockerfile/*.parquet"
  - config_name: "Dogescript"
    data_files:
      - split: train
        path: "data/Dogescript/*.parquet"
  - config_name: "Dylan"
    data_files:
      - split: train
        path: "data/Dylan/*.parquet"
  - config_name: "E"
    data_files:
      - split: train
        path: "data/E/*.parquet"
  - config_name: "E-mail"
    data_files:
      - split: train
        path: "data/E-mail/*.parquet"
  - config_name: "EBNF"
    data_files:
      - split: train
        path: "data/EBNF/*.parquet"
  - config_name: "ECL"
    data_files:
      - split: train
        path: "data/ECL/*.parquet"
  - config_name: "ECLiPSe"
    data_files:
      - split: train
        path: "data/ECLiPSe/*.parquet"
  - config_name: "EJS"
    data_files:
      - split: train
        path: "data/EJS/*.parquet"
  - config_name: "EQ"
    data_files:
      - split: train
        path: "data/EQ/*.parquet"
  - config_name: "Eagle"
    data_files:
      - split: train
        path: "data/Eagle/*.parquet"
  - config_name: "Earthly"
    data_files:
      - split: train
        path: "data/Earthly/*.parquet"
  - config_name: "Easybuild"
    data_files:
      - split: train
        path: "data/Easybuild/*.parquet"
  - config_name: "Ecere_Projects"
    data_files:
      - split: train
        path: "data/Ecere_Projects/*.parquet"
  - config_name: "EditorConfig"
    data_files:
      - split: train
        path: "data/EditorConfig/*.parquet"
  - config_name: "Edje_Data_Collection"
    data_files:
      - split: train
        path: "data/Edje_Data_Collection/*.parquet"
  - config_name: "Eiffel"
    data_files:
      - split: train
        path: "data/Eiffel/*.parquet"
  - config_name: "Elixir"
    data_files:
      - split: train
        path: "data/Elixir/*.parquet"
  - config_name: "Elm"
    data_files:
      - split: train
        path: "data/Elm/*.parquet"
  - config_name: "Elvish"
    data_files:
      - split: train
        path: "data/Elvish/*.parquet"
  - config_name: "Emacs_Lisp"
    data_files:
      - split: train
        path: "data/Emacs_Lisp/*.parquet"
  - config_name: "EmberScript"
    data_files:
      - split: train
        path: "data/EmberScript/*.parquet"
  - config_name: "Erlang"
    data_files:
      - split: train
        path: "data/Erlang/*.parquet"
  - config_name: "Euphoria"
    data_files:
      - split: train
        path: "data/Euphoria/*.parquet"
  - config_name: "F-Sharp"
    data_files:
      - split: train
        path: "data/F-Sharp/*.parquet"
  - config_name: "F-Star"
    data_files:
      - split: train
        path: "data/F-Star/*.parquet"
  - config_name: "FIGlet_Font"
    data_files:
      - split: train
        path: "data/FIGlet_Font/*.parquet"
  - config_name: "FLUX"
    data_files:
      - split: train
        path: "data/FLUX/*.parquet"
  - config_name: "Factor"
    data_files:
      - split: train
        path: "data/Factor/*.parquet"
  - config_name: "Fancy"
    data_files:
      - split: train
        path: "data/Fancy/*.parquet"
  - config_name: "Fantom"
    data_files:
      - split: train
        path: "data/Fantom/*.parquet"
  - config_name: "Faust"
    data_files:
      - split: train
        path: "data/Faust/*.parquet"
  - config_name: "Fennel"
    data_files:
      - split: train
        path: "data/Fennel/*.parquet"
  - config_name: "Filebench_WML"
    data_files:
      - split: train
        path: "data/Filebench_WML/*.parquet"
  - config_name: "Filterscript"
    data_files:
      - split: train
        path: "data/Filterscript/*.parquet"
  - config_name: "Fluent"
    data_files:
      - split: train
        path: "data/Fluent/*.parquet"
  - config_name: "Formatted"
    data_files:
      - split: train
        path: "data/Formatted/*.parquet"
  - config_name: "Forth"
    data_files:
      - split: train
        path: "data/Forth/*.parquet"
  - config_name: "Fortran"
    data_files:
      - split: train
        path: "data/Fortran/*.parquet"
  - config_name: "Fortran_Free_Form"
    data_files:
      - split: train
        path: "data/Fortran_Free_Form/*.parquet"
  - config_name: "FreeBasic"
    data_files:
      - split: train
        path: "data/FreeBasic/*.parquet"
  - config_name: "FreeMarker"
    data_files:
      - split: train
        path: "data/FreeMarker/*.parquet"
  - config_name: "Frege"
    data_files:
      - split: train
        path: "data/Frege/*.parquet"
  - config_name: "Futhark"
    data_files:
      - split: train
        path: "data/Futhark/*.parquet"
  - config_name: "G-code"
    data_files:
      - split: train
        path: "data/G-code/*.parquet"
  - config_name: "GAML"
    data_files:
      - split: train
        path: "data/GAML/*.parquet"
  - config_name: "GAMS"
    data_files:
      - split: train
        path: "data/GAMS/*.parquet"
  - config_name: "GAP"
    data_files:
      - split: train
        path: "data/GAP/*.parquet"
  - config_name: "GCC_Machine_Description"
    data_files:
      - split: train
        path: "data/GCC_Machine_Description/*.parquet"
  - config_name: "GDB"
    data_files:
      - split: train
        path: "data/GDB/*.parquet"
  - config_name: "GDScript"
    data_files:
      - split: train
        path: "data/GDScript/*.parquet"
  - config_name: "GEDCOM"
    data_files:
      - split: train
        path: "data/GEDCOM/*.parquet"
  - config_name: "GLSL"
    data_files:
      - split: train
        path: "data/GLSL/*.parquet"
  - config_name: "GN"
    data_files:
      - split: train
        path: "data/GN/*.parquet"
  - config_name: "GSC"
    data_files:
      - split: train
        path: "data/GSC/*.parquet"
  - config_name: "Game_Maker_Language"
    data_files:
      - split: train
        path: "data/Game_Maker_Language/*.parquet"
  - config_name: "Gemfile.lock"
    data_files:
      - split: train
        path: "data/Gemfile.lock/*.parquet"
  - config_name: "Gemini"
    data_files:
      - split: train
        path: "data/Gemini/*.parquet"
  - config_name: "Genero"
    data_files:
      - split: train
        path: "data/Genero/*.parquet"
  - config_name: "Genero_Forms"
    data_files:
      - split: train
        path: "data/Genero_Forms/*.parquet"
  - config_name: "Genie"
    data_files:
      - split: train
        path: "data/Genie/*.parquet"
  - config_name: "Genshi"
    data_files:
      - split: train
        path: "data/Genshi/*.parquet"
  - config_name: "Gentoo_Ebuild"
    data_files:
      - split: train
        path: "data/Gentoo_Ebuild/*.parquet"
  - config_name: "Gentoo_Eclass"
    data_files:
      - split: train
        path: "data/Gentoo_Eclass/*.parquet"
  - config_name: "Gerber_Image"
    data_files:
      - split: train
        path: "data/Gerber_Image/*.parquet"
  - config_name: "Gettext_Catalog"
    data_files:
      - split: train
        path: "data/Gettext_Catalog/*.parquet"
  - config_name: "Gherkin"
    data_files:
      - split: train
        path: "data/Gherkin/*.parquet"
  - config_name: "Git_Attributes"
    data_files:
      - split: train
        path: "data/Git_Attributes/*.parquet"
  - config_name: "Git_Config"
    data_files:
      - split: train
        path: "data/Git_Config/*.parquet"
  - config_name: "Git_Revision_List"
    data_files:
      - split: train
        path: "data/Git_Revision_List/*.parquet"
  - config_name: "Gleam"
    data_files:
      - split: train
        path: "data/Gleam/*.parquet"
  - config_name: "Glyph"
    data_files:
      - split: train
        path: "data/Glyph/*.parquet"
  - config_name: "Glyph_Bitmap_Distribution_Format"
    data_files:
      - split: train
        path: "data/Glyph_Bitmap_Distribution_Format/*.parquet"
  - config_name: "Gnuplot"
    data_files:
      - split: train
        path: "data/Gnuplot/*.parquet"
  - config_name: "Go"
    data_files:
      - split: train
        path: "data/Go/*.parquet"
  - config_name: "Go_Checksums"
    data_files:
      - split: train
        path: "data/Go_Checksums/*.parquet"
  - config_name: "Go_Module"
    data_files:
      - split: train
        path: "data/Go_Module/*.parquet"
  - config_name: "Golo"
    data_files:
      - split: train
        path: "data/Golo/*.parquet"
  - config_name: "Gosu"
    data_files:
      - split: train
        path: "data/Gosu/*.parquet"
  - config_name: "Grace"
    data_files:
      - split: train
        path: "data/Grace/*.parquet"
  - config_name: "Gradle"
    data_files:
      - split: train
        path: "data/Gradle/*.parquet"
  - config_name: "Grammatical_Framework"
    data_files:
      - split: train
        path: "data/Grammatical_Framework/*.parquet"
  - config_name: "GraphQL"
    data_files:
      - split: train
        path: "data/GraphQL/*.parquet"
  - config_name: "Graph_Modeling_Language"
    data_files:
      - split: train
        path: "data/Graph_Modeling_Language/*.parquet"
  - config_name: "Graphviz_(DOT)"
    data_files:
      - split: train
        path: "data/Graphviz_(DOT)/*.parquet"
  - config_name: "Groovy"
    data_files:
      - split: train
        path: "data/Groovy/*.parquet"
  - config_name: "Groovy_Server_Pages"
    data_files:
      - split: train
        path: "data/Groovy_Server_Pages/*.parquet"
  - config_name: "HAProxy"
    data_files:
      - split: train
        path: "data/HAProxy/*.parquet"
  - config_name: "HCL"
    data_files:
      - split: train
        path: "data/HCL/*.parquet"
  - config_name: "HLSL"
    data_files:
      - split: train
        path: "data/HLSL/*.parquet"
  - config_name: "HOCON"
    data_files:
      - split: train
        path: "data/HOCON/*.parquet"
  - config_name: "HTML"
    data_files:
      - split: train
        path: "data/HTML/*.parquet"
  - config_name: "HTML+ECR"
    data_files:
      - split: train
        path: "data/HTML+ECR/*.parquet"
  - config_name: "HTML+EEX"
    data_files:
      - split: train
        path: "data/HTML+EEX/*.parquet"
  - config_name: "HTML+ERB"
    data_files:
      - split: train
        path: "data/HTML+ERB/*.parquet"
  - config_name: "HTML+PHP"
    data_files:
      - split: train
        path: "data/HTML+PHP/*.parquet"
  - config_name: "HTML+Razor"
    data_files:
      - split: train
        path: "data/HTML+Razor/*.parquet"
  - config_name: "HTTP"
    data_files:
      - split: train
        path: "data/HTTP/*.parquet"
  - config_name: "HXML"
    data_files:
      - split: train
        path: "data/HXML/*.parquet"
  - config_name: "Hack"
    data_files:
      - split: train
        path: "data/Hack/*.parquet"
  - config_name: "Haml"
    data_files:
      - split: train
        path: "data/Haml/*.parquet"
  - config_name: "Handlebars"
    data_files:
      - split: train
        path: "data/Handlebars/*.parquet"
  - config_name: "Harbour"
    data_files:
      - split: train
        path: "data/Harbour/*.parquet"
  - config_name: "Haskell"
    data_files:
      - split: train
        path: "data/Haskell/*.parquet"
  - config_name: "Haxe"
    data_files:
      - split: train
        path: "data/Haxe/*.parquet"
  - config_name: "HiveQL"
    data_files:
      - split: train
        path: "data/HiveQL/*.parquet"
  - config_name: "HolyC"
    data_files:
      - split: train
        path: "data/HolyC/*.parquet"
  - config_name: "Hy"
    data_files:
      - split: train
        path: "data/Hy/*.parquet"
  - config_name: "HyPhy"
    data_files:
      - split: train
        path: "data/HyPhy/*.parquet"
  - config_name: "IDL"
    data_files:
      - split: train
        path: "data/IDL/*.parquet"
  - config_name: "IGOR_Pro"
    data_files:
      - split: train
        path: "data/IGOR_Pro/*.parquet"
  - config_name: "INI"
    data_files:
      - split: train
        path: "data/INI/*.parquet"
  - config_name: "IRC_log"
    data_files:
      - split: train
        path: "data/IRC_log/*.parquet"
  - config_name: "Idris"
    data_files:
      - split: train
        path: "data/Idris/*.parquet"
  - config_name: "Ignore_List"
    data_files:
      - split: train
        path: "data/Ignore_List/*.parquet"
  - config_name: "ImageJ_Macro"
    data_files:
      - split: train
        path: "data/ImageJ_Macro/*.parquet"
  - config_name: "Inform_7"
    data_files:
      - split: train
        path: "data/Inform_7/*.parquet"
  - config_name: "Inno_Setup"
    data_files:
      - split: train
        path: "data/Inno_Setup/*.parquet"
  - config_name: "Io"
    data_files:
      - split: train
        path: "data/Io/*.parquet"
  - config_name: "Ioke"
    data_files:
      - split: train
        path: "data/Ioke/*.parquet"
  - config_name: "Isabelle"
    data_files:
      - split: train
        path: "data/Isabelle/*.parquet"
  - config_name: "Isabelle_ROOT"
    data_files:
      - split: train
        path: "data/Isabelle_ROOT/*.parquet"
  - config_name: "J"
    data_files:
      - split: train
        path: "data/J/*.parquet"
  - config_name: "JAR_Manifest"
    data_files:
      - split: train
        path: "data/JAR_Manifest/*.parquet"
  - config_name: "JFlex"
    data_files:
      - split: train
        path: "data/JFlex/*.parquet"
  - config_name: "JSON"
    data_files:
      - split: train
        path: "data/JSON/*.parquet"
  - config_name: "JSON5"
    data_files:
      - split: train
        path: "data/JSON5/*.parquet"
  - config_name: "JSONLD"
    data_files:
      - split: train
        path: "data/JSONLD/*.parquet"
  - config_name: "JSON_with_Comments"
    data_files:
      - split: train
        path: "data/JSON_with_Comments/*.parquet"
  - config_name: "JSONiq"
    data_files:
      - split: train
        path: "data/JSONiq/*.parquet"
  - config_name: "Janet"
    data_files:
      - split: train
        path: "data/Janet/*.parquet"
  - config_name: "Jasmin"
    data_files:
      - split: train
        path: "data/Jasmin/*.parquet"
  - config_name: "Java"
    data_files:
      - split: train
        path: "data/Java/*.parquet"
  - config_name: "JavaScript"
    data_files:
      - split: train
        path: "data/JavaScript/*.parquet"
  - config_name: "JavaScript+ERB"
    data_files:
      - split: train
        path: "data/JavaScript+ERB/*.parquet"
  - config_name: "Java_Properties"
    data_files:
      - split: train
        path: "data/Java_Properties/*.parquet"
  - config_name: "Java_Server_Pages"
    data_files:
      - split: train
        path: "data/Java_Server_Pages/*.parquet"
  - config_name: "Jest_Snapshot"
    data_files:
      - split: train
        path: "data/Jest_Snapshot/*.parquet"
  - config_name: "JetBrains_MPS"
    data_files:
      - split: train
        path: "data/JetBrains_MPS/*.parquet"
  - config_name: "Jinja"
    data_files:
      - split: train
        path: "data/Jinja/*.parquet"
  - config_name: "Jison"
    data_files:
      - split: train
        path: "data/Jison/*.parquet"
  - config_name: "Jison_Lex"
    data_files:
      - split: train
        path: "data/Jison_Lex/*.parquet"
  - config_name: "Jolie"
    data_files:
      - split: train
        path: "data/Jolie/*.parquet"
  - config_name: "Jsonnet"
    data_files:
      - split: train
        path: "data/Jsonnet/*.parquet"
  - config_name: "Julia"
    data_files:
      - split: train
        path: "data/Julia/*.parquet"
  - config_name: "Jupyter_Notebook"
    data_files:
      - split: train
        path: "data/Jupyter_Notebook/*.parquet"
  - config_name: "KRL"
    data_files:
      - split: train
        path: "data/KRL/*.parquet"
  - config_name: "Kaitai_Struct"
    data_files:
      - split: train
        path: "data/Kaitai_Struct/*.parquet"
  - config_name: "KakouneScript"
    data_files:
      - split: train
        path: "data/KakouneScript/*.parquet"
  - config_name: "KiCad_Layout"
    data_files:
      - split: train
        path: "data/KiCad_Layout/*.parquet"
  - config_name: "KiCad_Legacy_Layout"
    data_files:
      - split: train
        path: "data/KiCad_Legacy_Layout/*.parquet"
  - config_name: "KiCad_Schematic"
    data_files:
      - split: train
        path: "data/KiCad_Schematic/*.parquet"
  - config_name: "Kit"
    data_files:
      - split: train
        path: "data/Kit/*.parquet"
  - config_name: "Kotlin"
    data_files:
      - split: train
        path: "data/Kotlin/*.parquet"
  - config_name: "Kusto"
    data_files:
      - split: train
        path: "data/Kusto/*.parquet"
  - config_name: "LFE"
    data_files:
      - split: train
        path: "data/LFE/*.parquet"
  - config_name: "LLVM"
    data_files:
      - split: train
        path: "data/LLVM/*.parquet"
  - config_name: "LOLCODE"
    data_files:
      - split: train
        path: "data/LOLCODE/*.parquet"
  - config_name: "LSL"
    data_files:
      - split: train
        path: "data/LSL/*.parquet"
  - config_name: "LTspice_Symbol"
    data_files:
      - split: train
        path: "data/LTspice_Symbol/*.parquet"
  - config_name: "LabVIEW"
    data_files:
      - split: train
        path: "data/LabVIEW/*.parquet"
  - config_name: "Lark"
    data_files:
      - split: train
        path: "data/Lark/*.parquet"
  - config_name: "Lasso"
    data_files:
      - split: train
        path: "data/Lasso/*.parquet"
  - config_name: "Latte"
    data_files:
      - split: train
        path: "data/Latte/*.parquet"
  - config_name: "Lean"
    data_files:
      - split: train
        path: "data/Lean/*.parquet"
  - config_name: "Less"
    data_files:
      - split: train
        path: "data/Less/*.parquet"
  - config_name: "Lex"
    data_files:
      - split: train
        path: "data/Lex/*.parquet"
  - config_name: "LigoLANG"
    data_files:
      - split: train
        path: "data/LigoLANG/*.parquet"
  - config_name: "LilyPond"
    data_files:
      - split: train
        path: "data/LilyPond/*.parquet"
  - config_name: "Limbo"
    data_files:
      - split: train
        path: "data/Limbo/*.parquet"
  - config_name: "Linker_Script"
    data_files:
      - split: train
        path: "data/Linker_Script/*.parquet"
  - config_name: "Linux_Kernel_Module"
    data_files:
      - split: train
        path: "data/Linux_Kernel_Module/*.parquet"
  - config_name: "Liquid"
    data_files:
      - split: train
        path: "data/Liquid/*.parquet"
  - config_name: "Literate_Agda"
    data_files:
      - split: train
        path: "data/Literate_Agda/*.parquet"
  - config_name: "Literate_CoffeeScript"
    data_files:
      - split: train
        path: "data/Literate_CoffeeScript/*.parquet"
  - config_name: "Literate_Haskell"
    data_files:
      - split: train
        path: "data/Literate_Haskell/*.parquet"
  - config_name: "LiveScript"
    data_files:
      - split: train
        path: "data/LiveScript/*.parquet"
  - config_name: "Logos"
    data_files:
      - split: train
        path: "data/Logos/*.parquet"
  - config_name: "Logtalk"
    data_files:
      - split: train
        path: "data/Logtalk/*.parquet"
  - config_name: "LookML"
    data_files:
      - split: train
        path: "data/LookML/*.parquet"
  - config_name: "LoomScript"
    data_files:
      - split: train
        path: "data/LoomScript/*.parquet"
  - config_name: "Lua"
    data_files:
      - split: train
        path: "data/Lua/*.parquet"
  - config_name: "M"
    data_files:
      - split: train
        path: "data/M/*.parquet"
  - config_name: "M4"
    data_files:
      - split: train
        path: "data/M4/*.parquet"
  - config_name: "M4Sugar"
    data_files:
      - split: train
        path: "data/M4Sugar/*.parquet"
  - config_name: "MATLAB"
    data_files:
      - split: train
        path: "data/MATLAB/*.parquet"
  - config_name: "MAXScript"
    data_files:
      - split: train
        path: "data/MAXScript/*.parquet"
  - config_name: "MLIR"
    data_files:
      - split: train
        path: "data/MLIR/*.parquet"
  - config_name: "MQL4"
    data_files:
      - split: train
        path: "data/MQL4/*.parquet"
  - config_name: "MQL5"
    data_files:
      - split: train
        path: "data/MQL5/*.parquet"
  - config_name: "MTML"
    data_files:
      - split: train
        path: "data/MTML/*.parquet"
  - config_name: "MUF"
    data_files:
      - split: train
        path: "data/MUF/*.parquet"
  - config_name: "Macaulay2"
    data_files:
      - split: train
        path: "data/Macaulay2/*.parquet"
  - config_name: "Makefile"
    data_files:
      - split: train
        path: "data/Makefile/*.parquet"
  - config_name: "Mako"
    data_files:
      - split: train
        path: "data/Mako/*.parquet"
  - config_name: "Markdown"
    data_files:
      - split: train
        path: "data/Markdown/*.parquet"
  - config_name: "Marko"
    data_files:
      - split: train
        path: "data/Marko/*.parquet"
  - config_name: "Mask"
    data_files:
      - split: train
        path: "data/Mask/*.parquet"
  - config_name: "Mathematica"
    data_files:
      - split: train
        path: "data/Mathematica/*.parquet"
  - config_name: "Maven_POM"
    data_files:
      - split: train
        path: "data/Maven_POM/*.parquet"
  - config_name: "Max"
    data_files:
      - split: train
        path: "data/Max/*.parquet"
  - config_name: "Mercury"
    data_files:
      - split: train
        path: "data/Mercury/*.parquet"
  - config_name: "Meson"
    data_files:
      - split: train
        path: "data/Meson/*.parquet"
  - config_name: "Metal"
    data_files:
      - split: train
        path: "data/Metal/*.parquet"
  - config_name: "Microsoft_Developer_Studio_Project"
    data_files:
      - split: train
        path: "data/Microsoft_Developer_Studio_Project/*.parquet"
  - config_name: "Microsoft_Visual_Studio_Solution"
    data_files:
      - split: train
        path: "data/Microsoft_Visual_Studio_Solution/*.parquet"
  - config_name: "MiniD"
    data_files:
      - split: train
        path: "data/MiniD/*.parquet"
  - config_name: "MiniYAML"
    data_files:
      - split: train
        path: "data/MiniYAML/*.parquet"
  - config_name: "Mint"
    data_files:
      - split: train
        path: "data/Mint/*.parquet"
  - config_name: "Mirah"
    data_files:
      - split: train
        path: "data/Mirah/*.parquet"
  - config_name: "Modelica"
    data_files:
      - split: train
        path: "data/Modelica/*.parquet"
  - config_name: "Modula-2"
    data_files:
      - split: train
        path: "data/Modula-2/*.parquet"
  - config_name: "Modula-3"
    data_files:
      - split: train
        path: "data/Modula-3/*.parquet"
  - config_name: "Module_Management_System"
    data_files:
      - split: train
        path: "data/Module_Management_System/*.parquet"
  - config_name: "Monkey"
    data_files:
      - split: train
        path: "data/Monkey/*.parquet"
  - config_name: "Monkey_C"
    data_files:
      - split: train
        path: "data/Monkey_C/*.parquet"
  - config_name: "Moocode"
    data_files:
      - split: train
        path: "data/Moocode/*.parquet"
  - config_name: "MoonScript"
    data_files:
      - split: train
        path: "data/MoonScript/*.parquet"
  - config_name: "Motoko"
    data_files:
      - split: train
        path: "data/Motoko/*.parquet"
  - config_name: "Motorola_68K_Assembly"
    data_files:
      - split: train
        path: "data/Motorola_68K_Assembly/*.parquet"
  - config_name: "Move"
    data_files:
      - split: train
        path: "data/Move/*.parquet"
  - config_name: "Muse"
    data_files:
      - split: train
        path: "data/Muse/*.parquet"
  - config_name: "Mustache"
    data_files:
      - split: train
        path: "data/Mustache/*.parquet"
  - config_name: "Myghty"
    data_files:
      - split: train
        path: "data/Myghty/*.parquet"
  - config_name: "NASL"
    data_files:
      - split: train
        path: "data/NASL/*.parquet"
  - config_name: "NCL"
    data_files:
      - split: train
        path: "data/NCL/*.parquet"
  - config_name: "NEON"
    data_files:
      - split: train
        path: "data/NEON/*.parquet"
  - config_name: "NL"
    data_files:
      - split: train
        path: "data/NL/*.parquet"
  - config_name: "NPM_Config"
    data_files:
      - split: train
        path: "data/NPM_Config/*.parquet"
  - config_name: "NSIS"
    data_files:
      - split: train
        path: "data/NSIS/*.parquet"
  - config_name: "NWScript"
    data_files:
      - split: train
        path: "data/NWScript/*.parquet"
  - config_name: "Nasal"
    data_files:
      - split: train
        path: "data/Nasal/*.parquet"
  - config_name: "Nearley"
    data_files:
      - split: train
        path: "data/Nearley/*.parquet"
  - config_name: "Nemerle"
    data_files:
      - split: train
        path: "data/Nemerle/*.parquet"
  - config_name: "NetLinx"
    data_files:
      - split: train
        path: "data/NetLinx/*.parquet"
  - config_name: "NetLinx+ERB"
    data_files:
      - split: train
        path: "data/NetLinx+ERB/*.parquet"
  - config_name: "NetLogo"
    data_files:
      - split: train
        path: "data/NetLogo/*.parquet"
  - config_name: "NewLisp"
    data_files:
      - split: train
        path: "data/NewLisp/*.parquet"
  - config_name: "Nextflow"
    data_files:
      - split: train
        path: "data/Nextflow/*.parquet"
  - config_name: "Nginx"
    data_files:
      - split: train
        path: "data/Nginx/*.parquet"
  - config_name: "Nim"
    data_files:
      - split: train
        path: "data/Nim/*.parquet"
  - config_name: "Ninja"
    data_files:
      - split: train
        path: "data/Ninja/*.parquet"
  - config_name: "Nit"
    data_files:
      - split: train
        path: "data/Nit/*.parquet"
  - config_name: "Nix"
    data_files:
      - split: train
        path: "data/Nix/*.parquet"
  - config_name: "Nu"
    data_files:
      - split: train
        path: "data/Nu/*.parquet"
  - config_name: "NumPy"
    data_files:
      - split: train
        path: "data/NumPy/*.parquet"
  - config_name: "Nunjucks"
    data_files:
      - split: train
        path: "data/Nunjucks/*.parquet"
  - config_name: "OCaml"
    data_files:
      - split: train
        path: "data/OCaml/*.parquet"
  - config_name: "ObjDump"
    data_files:
      - split: train
        path: "data/ObjDump/*.parquet"
  - config_name: "ObjectScript"
    data_files:
      - split: train
        path: "data/ObjectScript/*.parquet"
  - config_name: "Object_Data_Instance_Notation"
    data_files:
      - split: train
        path: "data/Object_Data_Instance_Notation/*.parquet"
  - config_name: "Objective-C"
    data_files:
      - split: train
        path: "data/Objective-C/*.parquet"
  - config_name: "Objective-C++"
    data_files:
      - split: train
        path: "data/Objective-C++/*.parquet"
  - config_name: "Objective-J"
    data_files:
      - split: train
        path: "data/Objective-J/*.parquet"
  - config_name: "Odin"
    data_files:
      - split: train
        path: "data/Odin/*.parquet"
  - config_name: "Omgrofl"
    data_files:
      - split: train
        path: "data/Omgrofl/*.parquet"
  - config_name: "Opa"
    data_files:
      - split: train
        path: "data/Opa/*.parquet"
  - config_name: "Opal"
    data_files:
      - split: train
        path: "data/Opal/*.parquet"
  - config_name: "OpenCL"
    data_files:
      - split: train
        path: "data/OpenCL/*.parquet"
  - config_name: "OpenEdge_ABL"
    data_files:
      - split: train
        path: "data/OpenEdge_ABL/*.parquet"
  - config_name: "OpenQASM"
    data_files:
      - split: train
        path: "data/OpenQASM/*.parquet"
  - config_name: "OpenRC_runscript"
    data_files:
      - split: train
        path: "data/OpenRC_runscript/*.parquet"
  - config_name: "OpenSCAD"
    data_files:
      - split: train
        path: "data/OpenSCAD/*.parquet"
  - config_name: "OpenStep_Property_List"
    data_files:
      - split: train
        path: "data/OpenStep_Property_List/*.parquet"
  - config_name: "OpenType_Feature_File"
    data_files:
      - split: train
        path: "data/OpenType_Feature_File/*.parquet"
  - config_name: "Open_Policy_Agent"
    data_files:
      - split: train
        path: "data/Open_Policy_Agent/*.parquet"
  - config_name: "Org"
    data_files:
      - split: train
        path: "data/Org/*.parquet"
  - config_name: "Ox"
    data_files:
      - split: train
        path: "data/Ox/*.parquet"
  - config_name: "Oxygene"
    data_files:
      - split: train
        path: "data/Oxygene/*.parquet"
  - config_name: "Oz"
    data_files:
      - split: train
        path: "data/Oz/*.parquet"
  - config_name: "P4"
    data_files:
      - split: train
        path: "data/P4/*.parquet"
  - config_name: "PEG.js"
    data_files:
      - split: train
        path: "data/PEG.js/*.parquet"
  - config_name: "PHP"
    data_files:
      - split: train
        path: "data/PHP/*.parquet"
  - config_name: "PLSQL"
    data_files:
      - split: train
        path: "data/PLSQL/*.parquet"
  - config_name: "PLpgSQL"
    data_files:
      - split: train
        path: "data/PLpgSQL/*.parquet"
  - config_name: "POV-Ray_SDL"
    data_files:
      - split: train
        path: "data/POV-Ray_SDL/*.parquet"
  - config_name: "Pan"
    data_files:
      - split: train
        path: "data/Pan/*.parquet"
  - config_name: "Papyrus"
    data_files:
      - split: train
        path: "data/Papyrus/*.parquet"
  - config_name: "Parrot"
    data_files:
      - split: train
        path: "data/Parrot/*.parquet"
  - config_name: "Parrot_Assembly"
    data_files:
      - split: train
        path: "data/Parrot_Assembly/*.parquet"
  - config_name: "Parrot_Internal_Representation"
    data_files:
      - split: train
        path: "data/Parrot_Internal_Representation/*.parquet"
  - config_name: "Pascal"
    data_files:
      - split: train
        path: "data/Pascal/*.parquet"
  - config_name: "Pawn"
    data_files:
      - split: train
        path: "data/Pawn/*.parquet"
  - config_name: "Pep8"
    data_files:
      - split: train
        path: "data/Pep8/*.parquet"
  - config_name: "Perl"
    data_files:
      - split: train
        path: "data/Perl/*.parquet"
  - config_name: "Pic"
    data_files:
      - split: train
        path: "data/Pic/*.parquet"
  - config_name: "Pickle"
    data_files:
      - split: train
        path: "data/Pickle/*.parquet"
  - config_name: "PicoLisp"
    data_files:
      - split: train
        path: "data/PicoLisp/*.parquet"
  - config_name: "PigLatin"
    data_files:
      - split: train
        path: "data/PigLatin/*.parquet"
  - config_name: "Pike"
    data_files:
      - split: train
        path: "data/Pike/*.parquet"
  - config_name: "PlantUML"
    data_files:
      - split: train
        path: "data/PlantUML/*.parquet"
  - config_name: "Pod"
    data_files:
      - split: train
        path: "data/Pod/*.parquet"
  - config_name: "Pod_6"
    data_files:
      - split: train
        path: "data/Pod_6/*.parquet"
  - config_name: "PogoScript"
    data_files:
      - split: train
        path: "data/PogoScript/*.parquet"
  - config_name: "Pony"
    data_files:
      - split: train
        path: "data/Pony/*.parquet"
  - config_name: "Portugol"
    data_files:
      - split: train
        path: "data/Portugol/*.parquet"
  - config_name: "PostCSS"
    data_files:
      - split: train
        path: "data/PostCSS/*.parquet"
  - config_name: "PostScript"
    data_files:
      - split: train
        path: "data/PostScript/*.parquet"
  - config_name: "PowerBuilder"
    data_files:
      - split: train
        path: "data/PowerBuilder/*.parquet"
  - config_name: "PowerShell"
    data_files:
      - split: train
        path: "data/PowerShell/*.parquet"
  - config_name: "Prisma"
    data_files:
      - split: train
        path: "data/Prisma/*.parquet"
  - config_name: "Processing"
    data_files:
      - split: train
        path: "data/Processing/*.parquet"
  - config_name: "Procfile"
    data_files:
      - split: train
        path: "data/Procfile/*.parquet"
  - config_name: "Proguard"
    data_files:
      - split: train
        path: "data/Proguard/*.parquet"
  - config_name: "Prolog"
    data_files:
      - split: train
        path: "data/Prolog/*.parquet"
  - config_name: "Promela"
    data_files:
      - split: train
        path: "data/Promela/*.parquet"
  - config_name: "Propeller_Spin"
    data_files:
      - split: train
        path: "data/Propeller_Spin/*.parquet"
  - config_name: "Protocol_Buffer"
    data_files:
      - split: train
        path: "data/Protocol_Buffer/*.parquet"
  - config_name: "Protocol_Buffer_Text_Format"
    data_files:
      - split: train
        path: "data/Protocol_Buffer_Text_Format/*.parquet"
  - config_name: "Public_Key"
    data_files:
      - split: train
        path: "data/Public_Key/*.parquet"
  - config_name: "Pug"
    data_files:
      - split: train
        path: "data/Pug/*.parquet"
  - config_name: "Puppet"
    data_files:
      - split: train
        path: "data/Puppet/*.parquet"
  - config_name: "PureBasic"
    data_files:
      - split: train
        path: "data/PureBasic/*.parquet"
  - config_name: "PureScript"
    data_files:
      - split: train
        path: "data/PureScript/*.parquet"
  - config_name: "Pure_Data"
    data_files:
      - split: train
        path: "data/Pure_Data/*.parquet"
  - config_name: "Python"
    data_files:
      - split: train
        path: "data/Python/*.parquet"
  - config_name: "Python_traceback"
    data_files:
      - split: train
        path: "data/Python_traceback/*.parquet"
  - config_name: "Q-Sharp"
    data_files:
      - split: train
        path: "data/Q-Sharp/*.parquet"
  - config_name: "QML"
    data_files:
      - split: train
        path: "data/QML/*.parquet"
  - config_name: "QMake"
    data_files:
      - split: train
        path: "data/QMake/*.parquet"
  - config_name: "Qt_Script"
    data_files:
      - split: train
        path: "data/Qt_Script/*.parquet"
  - config_name: "Quake"
    data_files:
      - split: train
        path: "data/Quake/*.parquet"
  - config_name: "R"
    data_files:
      - split: train
        path: "data/R/*.parquet"
  - config_name: "RAML"
    data_files:
      - split: train
        path: "data/RAML/*.parquet"
  - config_name: "RDoc"
    data_files:
      - split: train
        path: "data/RDoc/*.parquet"
  - config_name: "REALbasic"
    data_files:
      - split: train
        path: "data/REALbasic/*.parquet"
  - config_name: "REXX"
    data_files:
      - split: train
        path: "data/REXX/*.parquet"
  - config_name: "RMarkdown"
    data_files:
      - split: train
        path: "data/RMarkdown/*.parquet"
  - config_name: "RPC"
    data_files:
      - split: train
        path: "data/RPC/*.parquet"
  - config_name: "RPGLE"
    data_files:
      - split: train
        path: "data/RPGLE/*.parquet"
  - config_name: "RPM_Spec"
    data_files:
      - split: train
        path: "data/RPM_Spec/*.parquet"
  - config_name: "RUNOFF"
    data_files:
      - split: train
        path: "data/RUNOFF/*.parquet"
  - config_name: "Racket"
    data_files:
      - split: train
        path: "data/Racket/*.parquet"
  - config_name: "Ragel"
    data_files:
      - split: train
        path: "data/Ragel/*.parquet"
  - config_name: "Raku"
    data_files:
      - split: train
        path: "data/Raku/*.parquet"
  - config_name: "Rascal"
    data_files:
      - split: train
        path: "data/Rascal/*.parquet"
  - config_name: "Raw_token_data"
    data_files:
      - split: train
        path: "data/Raw_token_data/*.parquet"
  - config_name: "ReScript"
    data_files:
      - split: train
        path: "data/ReScript/*.parquet"
  - config_name: "Readline_Config"
    data_files:
      - split: train
        path: "data/Readline_Config/*.parquet"
  - config_name: "Reason"
    data_files:
      - split: train
        path: "data/Reason/*.parquet"
  - config_name: "ReasonLIGO"
    data_files:
      - split: train
        path: "data/ReasonLIGO/*.parquet"
  - config_name: "Rebol"
    data_files:
      - split: train
        path: "data/Rebol/*.parquet"
  - config_name: "Record_Jar"
    data_files:
      - split: train
        path: "data/Record_Jar/*.parquet"
  - config_name: "Red"
    data_files:
      - split: train
        path: "data/Red/*.parquet"
  - config_name: "Redcode"
    data_files:
      - split: train
        path: "data/Redcode/*.parquet"
  - config_name: "Redirect_Rules"
    data_files:
      - split: train
        path: "data/Redirect_Rules/*.parquet"
  - config_name: "Regular_Expression"
    data_files:
      - split: train
        path: "data/Regular_Expression/*.parquet"
  - config_name: "Ren-Py"
    data_files:
      - split: train
        path: "data/Ren-Py/*.parquet"
  - config_name: "RenderScript"
    data_files:
      - split: train
        path: "data/RenderScript/*.parquet"
  - config_name: "Rich_Text_Format"
    data_files:
      - split: train
        path: "data/Rich_Text_Format/*.parquet"
  - config_name: "Ring"
    data_files:
      - split: train
        path: "data/Ring/*.parquet"
  - config_name: "Riot"
    data_files:
      - split: train
        path: "data/Riot/*.parquet"
  - config_name: "RobotFramework"
    data_files:
      - split: train
        path: "data/RobotFramework/*.parquet"
  - config_name: "Roff"
    data_files:
      - split: train
        path: "data/Roff/*.parquet"
  - config_name: "Roff_Manpage"
    data_files:
      - split: train
        path: "data/Roff_Manpage/*.parquet"
  - config_name: "Rouge"
    data_files:
      - split: train
        path: "data/Rouge/*.parquet"
  - config_name: "RouterOS_Script"
    data_files:
      - split: train
        path: "data/RouterOS_Script/*.parquet"
  - config_name: "Ruby"
    data_files:
      - split: train
        path: "data/Ruby/*.parquet"
  - config_name: "Rust"
    data_files:
      - split: train
        path: "data/Rust/*.parquet"
  - config_name: "SAS"
    data_files:
      - split: train
        path: "data/SAS/*.parquet"
  - config_name: "SCSS"
    data_files:
      - split: train
        path: "data/SCSS/*.parquet"
  - config_name: "SELinux_Policy"
    data_files:
      - split: train
        path: "data/SELinux_Policy/*.parquet"
  - config_name: "SMT"
    data_files:
      - split: train
        path: "data/SMT/*.parquet"
  - config_name: "SPARQL"
    data_files:
      - split: train
        path: "data/SPARQL/*.parquet"
  - config_name: "SQF"
    data_files:
      - split: train
        path: "data/SQF/*.parquet"
  - config_name: "SQL"
    data_files:
      - split: train
        path: "data/SQL/*.parquet"
  - config_name: "SQLPL"
    data_files:
      - split: train
        path: "data/SQLPL/*.parquet"
  - config_name: "SRecode_Template"
    data_files:
      - split: train
        path: "data/SRecode_Template/*.parquet"
  - config_name: "SSH_Config"
    data_files:
      - split: train
        path: "data/SSH_Config/*.parquet"
  - config_name: "STAR"
    data_files:
      - split: train
        path: "data/STAR/*.parquet"
  - config_name: "STL"
    data_files:
      - split: train
        path: "data/STL/*.parquet"
  - config_name: "STON"
    data_files:
      - split: train
        path: "data/STON/*.parquet"
  - config_name: "SVG"
    data_files:
      - split: train
        path: "data/SVG/*.parquet"
  - config_name: "SWIG"
    data_files:
      - split: train
        path: "data/SWIG/*.parquet"
  - config_name: "Sage"
    data_files:
      - split: train
        path: "data/Sage/*.parquet"
  - config_name: "SaltStack"
    data_files:
      - split: train
        path: "data/SaltStack/*.parquet"
  - config_name: "Sass"
    data_files:
      - split: train
        path: "data/Sass/*.parquet"
  - config_name: "Scala"
    data_files:
      - split: train
        path: "data/Scala/*.parquet"
  - config_name: "Scaml"
    data_files:
      - split: train
        path: "data/Scaml/*.parquet"
  - config_name: "Scheme"
    data_files:
      - split: train
        path: "data/Scheme/*.parquet"
  - config_name: "Scilab"
    data_files:
      - split: train
        path: "data/Scilab/*.parquet"
  - config_name: "Self"
    data_files:
      - split: train
        path: "data/Self/*.parquet"
  - config_name: "ShaderLab"
    data_files:
      - split: train
        path: "data/ShaderLab/*.parquet"
  - config_name: "Shell"
    data_files:
      - split: train
        path: "data/Shell/*.parquet"
  - config_name: "ShellCheck_Config"
    data_files:
      - split: train
        path: "data/ShellCheck_Config/*.parquet"
  - config_name: "ShellSession"
    data_files:
      - split: train
        path: "data/ShellSession/*.parquet"
  - config_name: "Shen"
    data_files:
      - split: train
        path: "data/Shen/*.parquet"
  - config_name: "Sieve"
    data_files:
      - split: train
        path: "data/Sieve/*.parquet"
  - config_name: "Singularity"
    data_files:
      - split: train
        path: "data/Singularity/*.parquet"
  - config_name: "Slash"
    data_files:
      - split: train
        path: "data/Slash/*.parquet"
  - config_name: "Slice"
    data_files:
      - split: train
        path: "data/Slice/*.parquet"
  - config_name: "Slim"
    data_files:
      - split: train
        path: "data/Slim/*.parquet"
  - config_name: "SmPL"
    data_files:
      - split: train
        path: "data/SmPL/*.parquet"
  - config_name: "Smali"
    data_files:
      - split: train
        path: "data/Smali/*.parquet"
  - config_name: "Smalltalk"
    data_files:
      - split: train
        path: "data/Smalltalk/*.parquet"
  - config_name: "Smarty"
    data_files:
      - split: train
        path: "data/Smarty/*.parquet"
  - config_name: "Solidity"
    data_files:
      - split: train
        path: "data/Solidity/*.parquet"
  - config_name: "Soong"
    data_files:
      - split: train
        path: "data/Soong/*.parquet"
  - config_name: "SourcePawn"
    data_files:
      - split: train
        path: "data/SourcePawn/*.parquet"
  - config_name: "Spline_Font_Database"
    data_files:
      - split: train
        path: "data/Spline_Font_Database/*.parquet"
  - config_name: "Squirrel"
    data_files:
      - split: train
        path: "data/Squirrel/*.parquet"
  - config_name: "Stan"
    data_files:
      - split: train
        path: "data/Stan/*.parquet"
  - config_name: "Standard_ML"
    data_files:
      - split: train
        path: "data/Standard_ML/*.parquet"
  - config_name: "Starlark"
    data_files:
      - split: train
        path: "data/Starlark/*.parquet"
  - config_name: "Stata"
    data_files:
      - split: train
        path: "data/Stata/*.parquet"
  - config_name: "StringTemplate"
    data_files:
      - split: train
        path: "data/StringTemplate/*.parquet"
  - config_name: "Stylus"
    data_files:
      - split: train
        path: "data/Stylus/*.parquet"
  - config_name: "SubRip_Text"
    data_files:
      - split: train
        path: "data/SubRip_Text/*.parquet"
  - config_name: "SugarSS"
    data_files:
      - split: train
        path: "data/SugarSS/*.parquet"
  - config_name: "SuperCollider"
    data_files:
      - split: train
        path: "data/SuperCollider/*.parquet"
  - config_name: "Svelte"
    data_files:
      - split: train
        path: "data/Svelte/*.parquet"
  - config_name: "Swift"
    data_files:
      - split: train
        path: "data/Swift/*.parquet"
  - config_name: "SystemVerilog"
    data_files:
      - split: train
        path: "data/SystemVerilog/*.parquet"
  - config_name: "TI_Program"
    data_files:
      - split: train
        path: "data/TI_Program/*.parquet"
  - config_name: "TLA"
    data_files:
      - split: train
        path: "data/TLA/*.parquet"
  - config_name: "TOML"
    data_files:
      - split: train
        path: "data/TOML/*.parquet"
  - config_name: "TSQL"
    data_files:
      - split: train
        path: "data/TSQL/*.parquet"
  - config_name: "TSV"
    data_files:
      - split: train
        path: "data/TSV/*.parquet"
  - config_name: "TSX"
    data_files:
      - split: train
        path: "data/TSX/*.parquet"
  - config_name: "TXL"
    data_files:
      - split: train
        path: "data/TXL/*.parquet"
  - config_name: "Talon"
    data_files:
      - split: train
        path: "data/Talon/*.parquet"
  - config_name: "Tcl"
    data_files:
      - split: train
        path: "data/Tcl/*.parquet"
  - config_name: "Tcsh"
    data_files:
      - split: train
        path: "data/Tcsh/*.parquet"
  - config_name: "TeX"
    data_files:
      - split: train
        path: "data/TeX/*.parquet"
  - config_name: "Tea"
    data_files:
      - split: train
        path: "data/Tea/*.parquet"
  - config_name: "Terra"
    data_files:
      - split: train
        path: "data/Terra/*.parquet"
  - config_name: "Texinfo"
    data_files:
      - split: train
        path: "data/Texinfo/*.parquet"
  - config_name: "Text"
    data_files:
      - split: train
        path: "data/Text/*.parquet"
  - config_name: "TextMate_Properties"
    data_files:
      - split: train
        path: "data/TextMate_Properties/*.parquet"
  - config_name: "Textile"
    data_files:
      - split: train
        path: "data/Textile/*.parquet"
  - config_name: "Thrift"
    data_files:
      - split: train
        path: "data/Thrift/*.parquet"
  - config_name: "Turing"
    data_files:
      - split: train
        path: "data/Turing/*.parquet"
  - config_name: "Turtle"
    data_files:
      - split: train
        path: "data/Turtle/*.parquet"
  - config_name: "Twig"
    data_files:
      - split: train
        path: "data/Twig/*.parquet"
  - config_name: "TypeScript"
    data_files:
      - split: train
        path: "data/TypeScript/*.parquet"
  - config_name: "Type_Language"
    data_files:
      - split: train
        path: "data/Type_Language/*.parquet"
  - config_name: "Unified_Parallel_C"
    data_files:
      - split: train
        path: "data/Unified_Parallel_C/*.parquet"
  - config_name: "Unity3D_Asset"
    data_files:
      - split: train
        path: "data/Unity3D_Asset/*.parquet"
  - config_name: "Unix_Assembly"
    data_files:
      - split: train
        path: "data/Unix_Assembly/*.parquet"
  - config_name: "Uno"
    data_files:
      - split: train
        path: "data/Uno/*.parquet"
  - config_name: "UnrealScript"
    data_files:
      - split: train
        path: "data/UnrealScript/*.parquet"
  - config_name: "UrWeb"
    data_files:
      - split: train
        path: "data/UrWeb/*.parquet"
  - config_name: "V"
    data_files:
      - split: train
        path: "data/V/*.parquet"
  - config_name: "VBA"
    data_files:
      - split: train
        path: "data/VBA/*.parquet"
  - config_name: "VBScript"
    data_files:
      - split: train
        path: "data/VBScript/*.parquet"
  - config_name: "VCL"
    data_files:
      - split: train
        path: "data/VCL/*.parquet"
  - config_name: "VHDL"
    data_files:
      - split: train
        path: "data/VHDL/*.parquet"
  - config_name: "Vala"
    data_files:
      - split: train
        path: "data/Vala/*.parquet"
  - config_name: "Valve_Data_Format"
    data_files:
      - split: train
        path: "data/Valve_Data_Format/*.parquet"
  - config_name: "Velocity_Template_Language"
    data_files:
      - split: train
        path: "data/Velocity_Template_Language/*.parquet"
  - config_name: "Verilog"
    data_files:
      - split: train
        path: "data/Verilog/*.parquet"
  - config_name: "Vim_Help_File"
    data_files:
      - split: train
        path: "data/Vim_Help_File/*.parquet"
  - config_name: "Vim_Script"
    data_files:
      - split: train
        path: "data/Vim_Script/*.parquet"
  - config_name: "Vim_Snippet"
    data_files:
      - split: train
        path: "data/Vim_Snippet/*.parquet"
  - config_name: "Visual_Basic_.NET"
    data_files:
      - split: train
        path: "data/Visual_Basic_.NET/*.parquet"
  - config_name: "Volt"
    data_files:
      - split: train
        path: "data/Volt/*.parquet"
  - config_name: "Vue"
    data_files:
      - split: train
        path: "data/Vue/*.parquet"
  - config_name: "Vyper"
    data_files:
      - split: train
        path: "data/Vyper/*.parquet"
  - config_name: "Wavefront_Material"
    data_files:
      - split: train
        path: "data/Wavefront_Material/*.parquet"
  - config_name: "Wavefront_Object"
    data_files:
      - split: train
        path: "data/Wavefront_Object/*.parquet"
  - config_name: "WebAssembly"
    data_files:
      - split: train
        path: "data/WebAssembly/*.parquet"
  - config_name: "WebIDL"
    data_files:
      - split: train
        path: "data/WebIDL/*.parquet"
  - config_name: "WebVTT"
    data_files:
      - split: train
        path: "data/WebVTT/*.parquet"
  - config_name: "Web_Ontology_Language"
    data_files:
      - split: train
        path: "data/Web_Ontology_Language/*.parquet"
  - config_name: "Wget_Config"
    data_files:
      - split: train
        path: "data/Wget_Config/*.parquet"
  - config_name: "Whiley"
    data_files:
      - split: train
        path: "data/Whiley/*.parquet"
  - config_name: "Wikitext"
    data_files:
      - split: train
        path: "data/Wikitext/*.parquet"
  - config_name: "Win32_Message_File"
    data_files:
      - split: train
        path: "data/Win32_Message_File/*.parquet"
  - config_name: "Windows_Registry_Entries"
    data_files:
      - split: train
        path: "data/Windows_Registry_Entries/*.parquet"
  - config_name: "Witcher_Script"
    data_files:
      - split: train
        path: "data/Witcher_Script/*.parquet"
  - config_name: "Wollok"
    data_files:
      - split: train
        path: "data/Wollok/*.parquet"
  - config_name: "World_of_Warcraft_Addon_Data"
    data_files:
      - split: train
        path: "data/World_of_Warcraft_Addon_Data/*.parquet"
  - config_name: "Wren"
    data_files:
      - split: train
        path: "data/Wren/*.parquet"
  - config_name: "X10"
    data_files:
      - split: train
        path: "data/X10/*.parquet"
  - config_name: "XC"
    data_files:
      - split: train
        path: "data/XC/*.parquet"
  - config_name: "XCompose"
    data_files:
      - split: train
        path: "data/XCompose/*.parquet"
  - config_name: "XML"
    data_files:
      - split: train
        path: "data/XML/*.parquet"
  - config_name: "XML_Property_List"
    data_files:
      - split: train
        path: "data/XML_Property_List/*.parquet"
  - config_name: "XPages"
    data_files:
      - split: train
        path: "data/XPages/*.parquet"
  - config_name: "XProc"
    data_files:
      - split: train
        path: "data/XProc/*.parquet"
  - config_name: "XQuery"
    data_files:
      - split: train
        path: "data/XQuery/*.parquet"
  - config_name: "XS"
    data_files:
      - split: train
        path: "data/XS/*.parquet"
  - config_name: "XSLT"
    data_files:
      - split: train
        path: "data/XSLT/*.parquet"
  - config_name: "X_BitMap"
    data_files:
      - split: train
        path: "data/X_BitMap/*.parquet"
  - config_name: "X_Font_Directory_Index"
    data_files:
      - split: train
        path: "data/X_Font_Directory_Index/*.parquet"
  - config_name: "X_PixMap"
    data_files:
      - split: train
        path: "data/X_PixMap/*.parquet"
  - config_name: "Xojo"
    data_files:
      - split: train
        path: "data/Xojo/*.parquet"
  - config_name: "Xonsh"
    data_files:
      - split: train
        path: "data/Xonsh/*.parquet"
  - config_name: "Xtend"
    data_files:
      - split: train
        path: "data/Xtend/*.parquet"
  - config_name: "YAML"
    data_files:
      - split: train
        path: "data/YAML/*.parquet"
  - config_name: "YANG"
    data_files:
      - split: train
        path: "data/YANG/*.parquet"
  - config_name: "YARA"
    data_files:
      - split: train
        path: "data/YARA/*.parquet"
  - config_name: "YASnippet"
    data_files:
      - split: train
        path: "data/YASnippet/*.parquet"
  - config_name: "Yacc"
    data_files:
      - split: train
        path: "data/Yacc/*.parquet"
  - config_name: "Yul"
    data_files:
      - split: train
        path: "data/Yul/*.parquet"
  - config_name: "ZAP"
    data_files:
      - split: train
        path: "data/ZAP/*.parquet"
  - config_name: "ZIL"
    data_files:
      - split: train
        path: "data/ZIL/*.parquet"
  - config_name: "Zeek"
    data_files:
      - split: train
        path: "data/Zeek/*.parquet"
  - config_name: "ZenScript"
    data_files:
      - split: train
        path: "data/ZenScript/*.parquet"
  - config_name: "Zephir"
    data_files:
      - split: train
        path: "data/Zephir/*.parquet"
  - config_name: "Zig"
    data_files:
      - split: train
        path: "data/Zig/*.parquet"
  - config_name: "Zimpl"
    data_files:
      - split: train
        path: "data/Zimpl/*.parquet"
  - config_name: "cURL_Config"
    data_files:
      - split: train
        path: "data/cURL_Config/*.parquet"
  - config_name: "desktop"
    data_files:
      - split: train
        path: "data/desktop/*.parquet"
  - config_name: "dircolors"
    data_files:
      - split: train
        path: "data/dircolors/*.parquet"
  - config_name: "eC"
    data_files:
      - split: train
        path: "data/eC/*.parquet"
  - config_name: "edn"
    data_files:
      - split: train
        path: "data/edn/*.parquet"
  - config_name: "fish"
    data_files:
      - split: train
        path: "data/fish/*.parquet"
  - config_name: "hoon"
    data_files:
      - split: train
        path: "data/hoon/*.parquet"
  - config_name: "jq"
    data_files:
      - split: train
        path: "data/jq/*.parquet"
  - config_name: "kvlang"
    data_files:
      - split: train
        path: "data/kvlang/*.parquet"
  - config_name: "mIRC_Script"
    data_files:
      - split: train
        path: "data/mIRC_Script/*.parquet"
  - config_name: "mcfunction"
    data_files:
      - split: train
        path: "data/mcfunction/*.parquet"
  - config_name: "mupad"
    data_files:
      - split: train
        path: "data/mupad/*.parquet"
  - config_name: "nanorc"
    data_files:
      - split: train
        path: "data/nanorc/*.parquet"
  - config_name: "nesC"
    data_files:
      - split: train
        path: "data/nesC/*.parquet"
  - config_name: "ooc"
    data_files:
      - split: train
        path: "data/ooc/*.parquet"
  - config_name: "q"
    data_files:
      - split: train
        path: "data/q/*.parquet"
  - config_name: "reStructuredText"
    data_files:
      - split: train
        path: "data/reStructuredText/*.parquet"
  - config_name: "robots.txt"
    data_files:
      - split: train
        path: "data/robots.txt/*.parquet"
  - config_name: "sed"
    data_files:
      - split: train
        path: "data/sed/*.parquet"
  - config_name: "wdl"
    data_files:
      - split: train
        path: "data/wdl/*.parquet"
  - config_name: "wisp"
    data_files:
      - split: train
        path: "data/wisp/*.parquet"
  - config_name: "xBase"
    data_files:
      - split: train
        path: "data/xBase/*.parquet"
---

# The Stack v2

<center>
    <img src="https://huggingface.co/datasets/bigcode/admin_private/resolve/main/thestackv2_banner.png" alt="Stackv2" width="900" height="600">
</center>

## Dataset Description

- **Homepage:** https://www.bigcode-project.org/
- **Repository:** https://github.com/bigcode-project
- **Paper:** [Link](https://huggingface.co/papers/2402.19173)
- **Point of Contact:** contact@bigcode-project.org

The dataset consists of 4 versions:

- [`bigcode/the-stack-v2`](https://huggingface.co/datasets/bigcode/the-stack-v2): the full "The Stack v2" dataset **<-- you are here**
- [`bigcode/the-stack-v2-dedup`](https://huggingface.co/datasets/bigcode/the-stack-v2-dedup): based on the `bigcode/the-stack-v2` but further near-deduplicated
- [`bigcode/the-stack-v2-train-full-ids`](https://huggingface.co/datasets/bigcode/the-stack-v2-train-full-ids): based on the `bigcode/the-stack-v2-dedup` dataset but further filtered with heuristics and spanning 600+ programming languages. The data is grouped into repositories.
- [`bigcode/the-stack-v2-train-smol-ids`](https://huggingface.co/datasets/bigcode/the-stack-v2-train-smol-ids): based on the `bigcode/the-stack-v2-dedup` dataset but further filtered with heuristics and spanning 17 programming languages. The data is grouped into repositories.

**These datasets only contain the SWHIDs to download the code files and not the content of the files itself. See examples below to see how to download content. We are working on making the training datasets available in the coming weeks.**

The Stack v2 is significantly larger than v1:

||The Stack v1|The Stack v2|
|-|-|-|
| full | 6.4TB | 67.5TB |
| dedup | 2.9TB | 32.1TB | 
| train (full) | ~200B tokens | ~900B tokens |


### Changelog

|Release|Description|
|-|-|
| v2.2.0 | Removed repositories that opted out before 2026-07-29. Removed repos from users and orgs that aren't on GitHub anymore |
| v2.1.0 | Removed repositories that opted out before 2024-04-09. Removed unreachable/private repositories (according to SWH) |
| v2.0.1 | Removed repositories that opted out before 2023-10-20. StarCoder2 was trained on this version |
| v2.0 | Initial release of the Stack v2 |

### Dataset Summary

The Stack v2 contains over 3B files in 600+ programming and markup languages. The dataset was created as part of the [BigCode Project](https://www.bigcode-project.org/), an open scientific collaboration working on the responsible development of Large Language Models for Code (Code LLMs). The Stack serves as a pre-training dataset for Code LLMs, i.e., code-generating AI systems which enable the synthesis of programs from natural language descriptions as well as other from code snippets.

This dataset is derived from the Software Heritage archive, the largest public archive of software source code and accompanying development history. Software Heritage is an open, non profit initiative to collect, preserve, and share the source code of all publicly available software, launched by Inria, in partnership with UNESCO. We acknowledge Software Heritage for providing access to this invaluable resource. For more details, visit the [Software Heritage website](https://www.softwareheritage.org).

### Languages

The dataset contains 658 languages. The full list can be found in the [language stats table](https://huggingface.co/datasets/bigcode/the-stack-v2/blob/main/language_stats.csv).

### How to use it

```python
from datasets import load_dataset

# full dataset (file IDs only)
ds = load_dataset("bigcode/the-stack-v2", split="train")

# specific language (e.g. Dockerfiles)
ds = load_dataset("bigcode/the-stack-v2", "Dockerfile", split="train")

# dataset streaming (will only download the data as needed)
ds = load_dataset("bigcode/the-stack-v2", streaming=True, split="train")
for sample in iter(ds): 
    print(sample) 
```

#### Downloading the file contents

The file contents are stored in the Software Heritage S3 bucket to ensure data compliance. Downloading data in bulk requires an agreement with SoftwareHeritage and INRIA as stated in the dataset agreement.
Make sure to configure your environment with your [AWS credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html#examples). 

```bash
pip install smart_open[s3]
```

```python
import os
import boto3
from smart_open import open
from datasets import load_dataset

session = boto3.Session(
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
s3 = session.client("s3")

def download_contents(blob_id, src_encoding):
    s3_url = f"s3://softwareheritage/content/{blob_id}"
    
    with open(s3_url, "rb", compression=".gz", transport_params={"client": s3}) as fin:
        content = fin.read().decode(src_encoding)
    
    return {"content": content}

ds = load_dataset("bigcode/the-stack-v2", split="train", streaming=True)
ds = ds.map(lambda row: download_contents(row["blob_id"], row["src_encoding"]))
for row in ds:
    print(row["content"])
    break
```

## Dataset Structure

### Data Fields

* `blob_id` (`string`): Software Heritage (SWH) ID of the file on AWS S3.
* `directory_id` (`string`): SWH ID of the root directory of the repository.
* `path` (`string`): The file path within the repository.
* `content_id` (`string`): SWH content ID.
* `detected_licenses` (`string[]`): List of licenses (SPDX) detected by ScanCode.
* `license_type` (`string`): Inferred license type (`permissive` or `no_license`).
* `repo_name` (`string`): Repository name on GitHub.
* `snapshot_id` (`string`): SWH snapshot ID.
* `revision_id` (`string`): SWH revision (commit) ID.
* `branch_name` (`string`): Repository branch name.
* `visit_date` (`timestamp[ns]`): SWH crawl (snapshot) timestamp.
* `revision_date` (`timestamp[ns]`): SWH revision (commit) timestamp.
* `committer_date` (`timestamp[ns]`): SWH revision (commit) timestamp reported by the committer.
* `github_id` (`int64`): GitHub identifier for the repository.
* `star_events_count` (`int64`): number of stars calculated from GHArchive events.
* `fork_events_count` (`int64`): number of forks calculated from GHArchive events.
* `gha_license_id` (`string`): GHArchive SPDX license identifier, `None` if the repo is missing.
* `gha_event_created_at` (`timestamp[ns]`): Timestamp of the latest event on GHArchive for this repository.
* `gha_created_at` (`timestamp[ns]`): Timestamp of repository creation on GitHub, `None` if the repo is missing.
* `gha_language` (`string`): Repository's primary programming language on GitHub, `None` if the repo is missing.
* `src_encoding` (`string`): Original encoding of the file content befre converting to UTF-8.
* `language` (`string`): Programming language of the file, detected by `go-enry / linguist`.
* `is_vendor` (`bool`): Indicator of vendor file (external library), detected by `go-enry`.
* `is_generated` (`bool`): Indicator of generated file (external library), detected by `go-enry`.
* `length_bytes` (`int64`): Length of the file content in UTF-8 bytes.
* `extension` (`string`): File extension.

### Data Splits

The dataset has no splits and all data is loaded as train split by default. If you want to setup a custom train-test split beware that dataset contains a lot of near-duplicates which can cause leakage into the test split.

## Dataset Creation

For more information on the dataset creation pipeline please refer to the [technical report](https://huggingface.co/papers/2402.19173).

### Curation Rationale
One of the challenges faced by researchers working on code LLMs is the lack of openness and transparency around the development of these systems. Most prior works described the high-level data collection process but did not release the training data. It is therefore difficult for other researchers to fully reproduce these models and understand what kind of pre-training data leads to high-performing code LLMs. By releasing an open large-scale code dataset we hope to make training of code LLMs more reproducible.

### Source Data

#### Data Collection

3.28B unique files belonging to 104.2M github repositories were collected by traversing the Software Heritage [2023-09-06](https://docs.softwareheritage.org/devel/swh-dataset/graph/dataset.html#graph-dataset-2023-09-06) graph dataset.
Additional repository-level metadata was collected from [GitHub Archive](https://www.gharchive.org/) data up to 2023-09-14.
The total uncompressed size of all files is 67.53TB.
Near-deduplication was implemented in the pre-processing pipeline on top of exact deduplication. 
Roughly 40% of permissively licensed files were (near-)duplicates.

The following are not stored:

* Files that cannot contribute to training code: binary, empty, could not be decoded
* Files larger than 10MB

**Training Datasets**: For the training datasets the programming languages were filtered further to 17 and 600+ for the `the-stack-v2-smol-ids` and `the-stack-v2-full-ids` dataset, respecively. In addition, heuristics were applied to further increase the quality of the dataset. The code files are also grouped into repositories to allow to pretrain with full repository context. For more details see the [technical report](https://drive.google.com/file/d/17iGn3c-sYNiLyRSY-A85QOzgzGnGiVI3/view?usp=sharing).

##### License detection 

We extract repository-level license information from [GH Archive](https://www.gharchive.org/) for all repositories with matching names in the SWH dataset. 
When the repo-level license is not available, i.e., for 96.93\% of repositories, we use the [ScanCode Toolkit](https://github.com/nexB/scancode-toolkit) to detect file-level licenses as follows:
* Find all filenames that could contain a license (e.g., LICENSE, MIT.txt, Apache2.0) or contain a reference to the license (e.g., README.md, GUIDELINES);
* Apply ScanCode's license detection to the matching files and gather the SPDX IDs of the detected licenses;
* Propagate the detected licenses to all files that have the same base path within the repository as the license file. 

The licenses we consider permissive are listed [here](https://huggingface.co/datasets/bigcode/the-stack-v2/blob/main/license_stats.csv). 
This list was compiled from the licenses approved by the [Blue Oak Council](https://blueoakcouncil.org/list), 
as well as licenses categorized as "Permissive" or "Public Domain" by [ScanCode](https://scancode-licensedb.aboutcode.org/).

#### Who are the source language producers?

The source (code) language producers are users of GitHub that created unique repository names up until 2023-09-06 (cutoff date).

### Personal and Sensitive Information

The released dataset may contain sensitive information such as emails, IP addresses, and API/ssh keys that have previously been published to public repositories on GitHub. Deduplication has helped to reduce the amount of sensitive data that may exist. In the event that the dataset contains personal information, researchers should only use public, non-personal information in support of conducting and publishing their [open-access](https://en.wikipedia.org/wiki/Open_access) research. Personal information should not be used for spamming purposes, including sending unsolicited emails or selling of personal information. Complaints, removal requests, and "do not contact" requests can be sent to contact@bigcode-project.org.

### Opting out of The Stack v2

We are giving developers the ability to have their code removed from the dataset upon request. The process for submitting and enacting removal requests will keep evolving throughout the project as we receive feedback and build up more data governance tools.

You can check if your code is in The Stack v2 with the following ["Am I In The Stack?" Space](https://huggingface.co/spaces/HuggingFaceCode/in-the-stack). If you'd like to have your data removed from the dataset follow the [instructions on GitHub](https://github.com/bigcode-project/opt-out-v2).

## Considerations for Using the Data

### Social Impact of Dataset

The Stack v2 is an output of the BigCode Project. BigCode aims to be responsible by design and by default. The project is conducted in the spirit of Open Science, focused on the responsible development of LLMs for code.

With the release of The Stack v2, we aim to increase access, reproducibility, and transparency of code LLMs in the research community. Work to de-risk and improve on the implementation of ethical best practices of code LLMs is conducted in various BigCode working groups. The Legal, Ethics, and Governance working group has explored topics such as licensing (including copyleft and the intended use of permissively licensed code), attribution of generated code to original code, rights to restrict processing, the inclusion of Personally Identifiable Information (PII), and risks of malicious code, among other topics. This work is ongoing as of October 25th, 2022.

We expect code LLMs to enable people from diverse backgrounds to write higher quality code and develop low-code applications. Mission-critical software could become easier to maintain as professional developers are guided by code-generating systems on how to write more robust and efficient code. While the social impact is intended to be positive, the increased accessibility of code LLMs comes with certain risks such as over-reliance on the generated code and long-term effects on the software development job market.

A broader impact analysis relating to Code LLMs can be found in section 7 of this [paper](https://arxiv.org/abs/2107.03374). An in-depth risk assessments for Code LLMs can be found in section 4 of this [paper](https://arxiv.org/abs/2207.14157).

### Discussion of Biases 
The code collected from GitHub does not contain demographic information or proxy information about the demographics. However, it is not without risks,
as the comments within the code may contain harmful or offensive language, which could be learned by the models. 

Widely adopted programming languages like C and Javascript are overrepresented compared to niche programming languages like Julia and Scala. Some programming languages such as SQL, Batchfile, TypeScript are less likely to be permissively licensed (4% vs the average 10%). This may result in a biased representation of those languages. Permissively licensed files also tend to be longer.

The majority of natural language present in code from GitHub is English.

### Other Known Limitations

One of the current limitations of The Stack v2 is that scraped HTML for websites may not be compliant with Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). This could have an impact on HTML-generated code that may introduce web accessibility issues.

The training dataset could contain malicious code and/or the model could be used to generate malware or ransomware. 

To the best of our knowledge, all files contained in the dataset are licensed with one of the permissive licenses (see list in [Licensing information](#licensing-information)) or no license. 
The accuracy of license attribution is limited by the accuracy of GHArchive and ScanCode Toolkit. 
Any mistakes should be reported to BigCode Project for review and follow-up as needed. 

## Additional Information

### Dataset Curators
1. Harm de Vries, ServiceNow Research, harm.devries@servicenow.com
2. Leandro von Werra, Hugging Face, leandro@huggingface.co

### Licensing Information
The Stack v2 is a collection of source code from repositories with various licenses. Any use of all or part of the code gathered in The Stack v2 must abide by the terms of the original licenses, including attribution clauses when relevant. We facilitate this by providing provenance information for each data point.

The list of [SPDX license identifiers](https://spdx.org/licenses/) included in the dataset can be found [here](https://huggingface.co/datasets/bigcode/the-stack-v2/blob/main/license_stats.csv).

### Citation Information

```bash
@misc{lozhkov2024starcoder,
      title={StarCoder 2 and The Stack v2: The Next Generation}, 
      author={Anton Lozhkov and Raymond Li and Loubna Ben Allal and Federico Cassano and Joel Lamy-Poirier and Nouamane Tazi and Ao Tang and Dmytro Pykhtar and Jiawei Liu and Yuxiang Wei and Tianyang Liu and Max Tian and Denis Kocetkov and Arthur Zucker and Younes Belkada and Zijian Wang and Qian Liu and Dmitry Abulkhanov and Indraneil Paul and Zhuang Li and Wen-Ding Li and Megan Risdal and Jia Li and Jian Zhu and Terry Yue Zhuo and Evgenii Zheltonozhskii and Nii Osae Osae Dade and Wenhao Yu and Lucas Krauß and Naman Jain and Yixuan Su and Xuanli He and Manan Dey and Edoardo Abati and Yekun Chai and Niklas Muennighoff and Xiangru Tang and Muhtasham Oblokulov and Christopher Akiki and Marc Marone and Chenghao Mou and Mayank Mishra and Alex Gu and Binyuan Hui and Tri Dao and Armel Zebaze and Olivier Dehaene and Nicolas Patry and Canwen Xu and Julian McAuley and Han Hu and Torsten Scholak and Sebastien Paquet and Jennifer Robinson and Carolyn Jane Anderson and Nicolas Chapados and Mostofa Patwary and Nima Tajbakhsh and Yacine Jernite and Carlos Muñoz Ferrandis and Lingming Zhang and Sean Hughes and Thomas Wolf and Arjun Guha and Leandro von Werra and Harm de Vries},
      year={2024},
      eprint={2402.19173},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```
