| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join Condition |
|:----------:|:-----------------:|:------------:|:--------------:|:------------------:|:---:|
| Student | ex:fullname | ex:Person | | http://example.org/person/{Student} | |
| Sport | ex:sportname | ex:Sport | | http://example.org/person/{Sport} | |
|       | ex:practises | ex:Person| ex:Sport | http://example.org/person/{Student} | student=student, sport=sport |