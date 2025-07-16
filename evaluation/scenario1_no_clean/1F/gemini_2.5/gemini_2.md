| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join Condition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **student.csv** | | | | | |
| ID | ex:id | ex:Person | - | ex:person/{ID} | - |
| FirstName | ex:firstname | ex:Person | - | ex:person/{ID} | - |
| LastName | ex:lastname | ex:Person | - | ex:person/{ID} | - |
| FirstName, LastName | ex:fullname | ex:Person | - | ex:person/{ID} | - |
| **sport.csv** | | | | | |
| ID | ex:sportid | ex:Sport | - | ex:sport/{ID} | - |
| Description | ex:sportname | ex:Sport | - | ex:sport/{ID} | - |
| **student_sport.csv** | | | | | |
| ID_Student, ID_Sport | ex:practises | ex:Person | ex:Sport | ex:person/{ID_Student} | student.csv.ID == student_sport.csv.ID_Student AND sport.csv.ID == student_sport.csv.ID_Sport |
