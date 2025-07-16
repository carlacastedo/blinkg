| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join Condition | Datatype | Language Annotations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |:--- |
| `fname` (persons.csv) | `ex:firstname` | `ex:Person` | - | `ex:Person/{fname}-{lname}` | - | `xsd:string` | - |
| `lname` (persons.csv) | `ex:lastname` | `ex:Person` | - | `ex:Person/{fname}-{lname}` | - | `xsd:string` | - |
| `fname`, `lname` (persons.csv) | `ex:fullname` | `ex:Person` | - | `ex:Person/{fname}-{lname}` | - | `xsd:string` | - |
| `amount` (persons.csv) | `ex:owes` | `ex:Person` | - | `ex:Person/{fname}-{lname}` | - | `xsd:double` | - |
| `city` (lives.csv) | `ex:lives` | `ex:Person` | `ex:City` | Subject: `ex:Person/{fname}-{lname}` <br> Object: `ex:City/{city}` | `persons.fname == lives.fname` AND `persons.lname == lives.lname` | - | - |
| `city` (lives.csv) | `ex:cityname` | `ex:City` | - | `ex:City/{city}` | - | `xsd:langString` | `en` |
