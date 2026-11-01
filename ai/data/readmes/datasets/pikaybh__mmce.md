---
language:
- ko
- en
license: cc-by-nc-4.0
size_categories:
- 10K<n<100K
task_categories:
- question-answering
- multiple-choice
pretty_name: kocem:kocem_v2
dataset_info:
  Architectural_Planning:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 3
        num_bytes: 44985
        download_size: 44985
      - name: test
        num_examples: 461
        num_bytes: 1351376
        download_size: 1351376
      - name: val
        num_examples: 41
        num_bytes: 172420
        download_size: 172420
    dataset_size: 1568781
    description: |
      이 config는 dev, test, val split에 걸쳐 505개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Building_System:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 5
        num_bytes: 56228
        download_size: 56228
      - name: test
        num_examples: 367
        num_bytes: 1127373
        download_size: 1127373
      - name: val
        num_examples: 49
        num_bytes: 205973
        download_size: 205973
    dataset_size: 1389574
    description: |
      이 config는 dev, test, val split에 걸쳐 421개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Comprehensive_Understanding:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: bytes
        - name: path
          dtype: string
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 3
        num_bytes: 6301330
        download_size: 6301330
      - name: test
        num_examples: 161
        num_bytes: 145687595
        download_size: 145687595
      - name: val
        num_examples: 157
        num_bytes: 141844071
        download_size: 141844071
    dataset_size: 293832996
    description: |
      이 config는 dev, test, val split에 걸쳐 321개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Construction_Management:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 5
        num_bytes: 50705
        download_size: 50705
      - name: test
        num_examples: 488
        num_bytes: 1415168
        download_size: 1415168
      - name: val
        num_examples: 34
        num_bytes: 153250
        download_size: 153250
    dataset_size: 1619123
    description: |
      이 config는 dev, test, val split에 걸쳐 527개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Domain_Reasoning:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: string
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: bytes
        - name: path
          dtype: string
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: number
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 3
        num_bytes: 97949
        download_size: 97949
      - name: test
        num_examples: 255
        num_bytes: 20561602
        download_size: 20561602
      - name: val
        num_examples: 10
        num_bytes: 2025856
        download_size: 2025856
    dataset_size: 22685407
    description: |
      이 config는 dev, test, val split에 걸쳐 268개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, number, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Drawing_Interpretation:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: int64
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: string
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: bytes
        - name: path
          dtype: string
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: number
        dtype: int64
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
      - name: tasks
        dtype: string
    splits:
      - name: dev
        num_examples: 5
        num_bytes: 3684412
        download_size: 3684412
      - name: test
        num_examples: 141
        num_bytes: 43193959
        download_size: 43193959
      - name: val
        num_examples: 9
        num_bytes: 11919796
        download_size: 11919796
    dataset_size: 58798167
    description: |
      이 config는 dev, test, val split에 걸쳐 155개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, number, options, question, question_type, subfield, subject, tasks.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Interior:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 6
        num_bytes: 55345
        download_size: 55345
      - name: test
        num_examples: 357
        num_bytes: 1072123
        download_size: 1072123
      - name: val
        num_examples: 46
        num_bytes: 188894
        download_size: 188894
    dataset_size: 1316362
    description: |
      이 config는 dev, test, val split에 걸쳐 409개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Materials:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 8
        num_bytes: 79881
        download_size: 79881
      - name: test
        num_examples: 407
        num_bytes: 1188350
        download_size: 1188350
      - name: val
        num_examples: 43
        num_bytes: 164170
        download_size: 164170
    dataset_size: 1432401
    description: |
      이 config는 dev, test, val split에 걸쳐 458개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Safety_Management:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 4
        num_bytes: 59064
        download_size: 59064
      - name: test
        num_examples: 376
        num_bytes: 1211336
        download_size: 1211336
      - name: val
        num_examples: 41
        num_bytes: 161880
        download_size: 161880
    dataset_size: 1432280
    description: |
      이 config는 dev, test, val split에 걸쳐 421개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Standard_Nomenclature:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: difficulty
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: human_acc
        dtype: string
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: unknown
        - name: path
          dtype: unknown
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 5
        num_bytes: 21508
        download_size: 21508
      - name: test
        num_examples: 450
        num_bytes: 423163
        download_size: 423163
      - name: val
        num_examples: 45
        num_bytes: 63269
        download_size: 63269
    dataset_size: 507940
    description: |
      이 config는 dev, test, val split에 걸쳐 500개의 인스턴스를 포함합니다.
      Features: answer, answer_key, difficulty, eval_loop, exam, explanation, field, human_acc, id, image, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
  Structural_Engineering:
    features:
      - name: answer
        dtype: string
      - name: answer_key
        dtype: string
      - name: date
        dtype: string
      - name: difficulty
        dtype: string
      - name: en_answer
        dtype: string
      - name: en_explanation
        dtype: string
      - name: en_options
        dtype: string
      - name: en_question
        dtype: string
      - name: eval
        dtype: string
      - name: eval_loop
        dtype: string
      - name: exam
        dtype: string
      - name: explanation
        dtype: string
      - name: field
        dtype: string
      - name: field_feedback
        dtype: string
      - name: human_acc
        dtype: float64
      - name: human_feedback
        dtype: int64
      - name: id
        dtype: string
      - name: image
        struct:
        - name: bytes
          dtype: bytes
        - name: path
          dtype: string
      - name: ko_answer
        dtype: string
      - name: ko_explanation
        dtype: string
      - name: ko_options
        dtype: string
      - name: ko_question
        dtype: string
      - name: korean_national_technical_certification
        dtype: string
      - name: options
        dtype: string
      - name: question
        dtype: string
      - name: question_type
        dtype: string
      - name: subfield
        dtype: string
      - name: subject
        dtype: string
    splits:
      - name: dev
        num_examples: 2
        num_bytes: 54237
        download_size: 54237
      - name: test
        num_examples: 342
        num_bytes: 1480883
        download_size: 1480883
      - name: val
        num_examples: 34
        num_bytes: 177209
        download_size: 177209
    dataset_size: 1712329
    description: |
      이 config는 dev, test, val split에 걸쳐 378개의 인스턴스를 포함합니다.
      Features: answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject.
      주요 태그: Architectural_Planning, Building_System, Component Listing - Classification, Comprehensive Understanding, Construction Terminology, Construction_Management, Cost Estimating, Domain Knowledge, Domain Reasoning, Drawing Interpretation, Elevation, Error Detection/Supervision, Facility Plan, HVAC, Interior, MEP, Materials, Plumbing and Sanitary, Project Management, Quality Control, Quantity Calculation, Safety Engineering, Safety Technology, Safety Training, Section, Standard Nomenclature, Structural Engineering, Structural Plan, Structural_Engineering, multiple-choice.
configs:
- config_name: Architectural_Planning
  data_files:
  - split: dev
    path: Architectural_Planning/dev.parquet
  - split: test
    path: Architectural_Planning/test.parquet
  - split: val
    path: Architectural_Planning/val.parquet
- config_name: Building_System
  data_files:
  - split: dev
    path: Building_System/dev.parquet
  - split: test
    path: Building_System/test.parquet
  - split: val
    path: Building_System/val.parquet
- config_name: Comprehensive_Understanding
  data_files:
  - split: dev
    path: Comprehensive_Understanding/dev.parquet
  - split: test
    path: Comprehensive_Understanding/test.parquet
  - split: val
    path: Comprehensive_Understanding/val.parquet
- config_name: Construction_Management
  data_files:
  - split: dev
    path: Construction_Management/dev.parquet
  - split: test
    path: Construction_Management/test.parquet
  - split: val
    path: Construction_Management/val.parquet
- config_name: Domain_Reasoning
  data_files:
  - split: dev
    path: Domain_Reasoning/dev.parquet
  - split: test
    path: Domain_Reasoning/test.parquet
  - split: val
    path: Domain_Reasoning/val.parquet
- config_name: Drawing_Interpretation
  data_files:
  - split: dev
    path: Drawing_Interpretation/dev.parquet
  - split: test
    path: Drawing_Interpretation/test.parquet
  - split: val
    path: Drawing_Interpretation/val.parquet
- config_name: Interior
  data_files:
  - split: dev
    path: Interior/dev.parquet
  - split: test
    path: Interior/test.parquet
  - split: val
    path: Interior/val.parquet
- config_name: Materials
  data_files:
  - split: dev
    path: Materials/dev.parquet
  - split: test
    path: Materials/test.parquet
  - split: val
    path: Materials/val.parquet
- config_name: Safety_Management
  data_files:
  - split: dev
    path: Safety_Management/dev.parquet
  - split: test
    path: Safety_Management/test.parquet
  - split: val
    path: Safety_Management/val.parquet
- config_name: Standard_Nomenclature
  data_files:
  - split: dev
    path: Standard_Nomenclature/dev.parquet
  - split: test
    path: Standard_Nomenclature/test.parquet
  - split: val
    path: Standard_Nomenclature/val.parquet
- config_name: Structural_Engineering
  data_files:
  - split: dev
    path: Structural_Engineering/dev.parquet
  - split: test
    path: Structural_Engineering/test.parquet
  - split: val
    path: Structural_Engineering/val.parquet
tags:
- Architectural_Planning
- Building_System
- Component Listing - Classification
- Comprehensive Understanding
- Construction Terminology
- Construction_Management
- Cost Estimating
- Domain Knowledge
- Domain Reasoning
- Drawing Interpretation
- Elevation
- Error Detection/Supervision
- Facility Plan
- HVAC
- Interior
- MEP
- Materials
- Plumbing and Sanitary
- Project Management
- Quality Control
- Quantity Calculation
- Safety Engineering
- Safety Technology
- Safety Training
- Section
- Standard Nomenclature
- Structural Engineering
- Structural Plan
- Structural_Engineering
- multiple-choice
---

# KoCEM:KoCEM_v2

| Config | Splits | Features | Instances |
|--------|--------|----------|-----------|
| Architectural_Planning | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 505 |
| Building_System | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 421 |
| Comprehensive_Understanding | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 321 |
| Construction_Management | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 527 |
| Domain_Reasoning | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, number, options, question, question_type, subfield, subject | 268 |
| Drawing_Interpretation | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, number, options, question, question_type, subfield, subject, tasks | 155 |
| Interior | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 409 |
| Materials | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 458 |
| Safety_Management | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 421 |
| Standard_Nomenclature | dev, test, val | answer, answer_key, difficulty, eval_loop, exam, explanation, field, human_acc, id, image, korean_national_technical_certification, options, question, question_type, subfield, subject | 500 |
| Structural_Engineering | dev, test, val | answer, answer_key, date, difficulty, en_answer, en_explanation, en_options, en_question, eval, eval_loop, exam, explanation, field, field_feedback, human_acc, human_feedback, id, image, ko_answer, ko_explanation, ko_options, ko_question, korean_national_technical_certification, options, question, question_type, subfield, subject | 378 |
| **Total** |  |  | **4363** |
<div style="border: 2px solid #f87171; background-color: #fef2f2; border-radius: 12px; padding: 20px; margin: 20px 0; color: #991b1b; font-family: 'Segoe UI', 'Apple SD Gothic Neo', Arial, sans-serif; font-size: 1.05em;">
  <strong style="font-size:1.18em;">⚠️ Disclaimer</strong><br>
  Please note that this dataset was independently compiled for personal research purposes only.<br>
  I regret that I am unable to share access under any circumstances.<br>
  Accordingly, I kindly ask that you refrain from submitting access requests, as all such requests will have to be declined.<br>
  <u>Thank you very much for your understanding and consideration.</u>
</div>

## 문의

- pikaybh@snu.ac.kr
