| CSV Column     | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join Condition           | Datatype      | Language Annotations |
|---------------|------------------|-------------|---------------------|-------------------|------------------------|--------------|---------------------|
| fname        | ex:firstname      | ex:Person  | None                | Concatenate fname and lname as subject | Match fname and lname | xsd:string   | @en                 |
| lname        | ex:lastname       | ex:Person  | None                | Concatenate fname and lname as subject | Match fname and lname | xsd:string   | @en                 |
| amount       | ex:owes           | ex:Person  | None                | Concatenate fname and lname as subject | Match fname and lname | xsd:double   | None                |
| fname        | ex:firstname      | ex:Person  | None                | Concatenate fname and lname as subject | Match fname and lname | xsd:string   | @en                 |
| lname        | ex:lastname       | ex:Person  | None                | Concatenate fname and lname as subject | Match fname and lname | xsd:string   | @en                 |
| city         | ex:cityname       | ex:City    | None                | Use city name as subject               | Match city name       | xsd:langString | @en               |
| fname, lname | ex:lives          | ex:Person  | ex:City             | Concatenate fname and lname as subject for Person; Use city name as subject for City | Match fname and lname with city | N/A          | None                |
