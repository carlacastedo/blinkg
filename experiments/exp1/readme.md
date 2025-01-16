# Experiment 1

There are 11 test cases. For each one of them there is a prompt that is inserted in ChatGPT 4o and Microsoft Copilot. This prompt follows the next template.

```
I have these CSV files and I want to build a knowledge graph with all the relations in it. Could you make the graph and the corresponding mappings in RML? Make sure you reflect ALL de relations EXPLICITLY.
file1.csv 
Column 1, ..., Column N
...
file2.csv 
Column 1, ..., Column N
...
```

Both models brought back results for each of the test cases. Every mapping file generated is transformed in the corresponding knowledge graph with Morph-KGC. Sometimes the mapping files are not correct, and Morph-KGC cannot build the graph. Since the correction of the semantics is the topic of the study, the syntax is corrected manually in these cases.

All test cases are classified within four groups that reflect the difficulty level.

| Test case | Basic | Join | Link | Language |
|:--------:|:-----:|:----:|:----:|:--------:|
|01a|x||||
|02a|x||||
|04a|x||||
|05a|x||||
|08a|x||||
|09a||x|||
|10a|x||||
|11b|||x||
|12a|x||||
|12b|||x||
|15a||||x|

## Results

### 01a

#### Baseline

```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
```

#### GPT4o

```
<http://example.com/Student/Venus> <http://example.com/hasName> <http://example.com/Name/Venus> . 
<http://example.com/Student/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> . 
```

#### Copilot

```
<http://example.org/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.org/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
```

Both GPT4o and Copilot reflect more relations than the baseline graph, such as the type, that is taken from the context, as the name of the CSV file is `student.csv`.

### 02a

#### Baseline

```
<http://example.com/10/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
<http://example.com/10/Venus> <http://example.com/id> "10" .
<http://example.com/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

#### GPT4o

```
<http://example.org/student_10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
```
#### Copilot

```
<http://example.org/student/10> <http://example.org/hasID> "10" .
<http://example.org/student/10> <http://example.org/hasName> "Venus" .
<http://example.org/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .

```
Copilot makes a good first approach to the baseline graph, even though it uses different entities to represent the same concepts. In the other hand, GPT4o aproximation is very bad.

### 04a

#### Baseline

```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
<http://example.com/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
<http://example.com/Tennis> <http://xmlns.com/foaf/0.1/name> "Tennis" .
<http://example.com/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .

```

#### GPT4o

```
<http://example.org/student/Venus> <http://example.org/ns#plays> <http://example.org/sport/Tennis> .
<http://example.org/student/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```
#### Copilot

```
<http://example.com/student/Venus> <http://example.com/ns#plays> <http://example.com/sport/Tennis> .
<http://example.com/student/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ns#Student> .
```

In this case both models don't represent all the relations of the baseline explicitly. However, the URIs reflect that both classify Venus and Tennis as instances of Person/Student and Sport.

### 05a

#### Baseline

```
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Bob;Smith> <http://example.com/owes> "30.0E0" .
<http://example.com/Sue;Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Sue;Jones> <http://example.com/owes> "20.0E0" .
```

#### GPT4o

```
<http://example.org/person/Bob_Smith> <http://example.org/hasAmount> "http://example.org/amount/30.0E0"^^<http://www.w3.org/2001/XMLSchema#float> .
<http://example.org/person/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/person/Sue_Jones> <http://example.org/hasAmount> "http://example.org/amount/20.0E0"^^<http://www.w3.org/2001/XMLSchema#float> .
<http://example.org/person/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
```
#### Copilot

```
<http://example.org/Bob_Smith> <http://example.org/amount> "30.0E0" .
<http://example.org/Bob_Smith> <http://example.org/fname> "Bob" .
<http://example.org/Bob_Smith> <http://example.org/lname> "Smith" .
<http://example.org/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/Sue_Jones> <http://example.org/amount> "20.0E0" .
<http://example.org/Sue_Jones> <http://example.org/fname> "Sue" .
<http://example.org/Sue_Jones> <http://example.org/lname> "Jones" .
<http://example.org/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
```

Both models put the full names togheter in de URIs, following the baselines. However, Copilot makes explicit nodes for each part first and last names. In the baseline, the amount of money have the predicate `owes`, that in GPT4o is changed for `hasAmount` giving the data a different meaning. As there isn't enough context from de prompt, GP4o gives this interpretation. In the other hand, Copilot doesn't make assumptions and uses `amount` as predicate.

### 08a

#### Baseline

```
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10". 
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> "Tennis". 
```

#### GPT4o

```
<http://example.org/student/10> <http://dbpedia.org/ontology/sport> "Tennis" .
<http://example.org/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.org/student/10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```
#### Copilot

```
<http://example.org/10> <http://example.org/name> "Venus Williams" .
<http://example.org/10> <http://example.org/sport> "Tennis" .
<http://example.org/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
```
Both models make a correct approach.

### 09a

#### Baseline

```
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore"  .
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100>  .
```

#### GPT4o

```
<http://example.org/sport/100> <http://example.org/hasName> "Tennis" .
<http://example.org/sport/100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Sport> .
<http://example.org/student/10> <http://example.org/hasName> "Venus Williams" .
<http://example.org/student/10> <http://example.org/playsSport> <http://example.org/sport/100> .
<http://example.org/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
<http://example.org/student/20> <http://example.org/hasName> "Demi Moore" .
<http://example.org/student/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
```
#### Copilot

```
<http://example.com/sport/100> <http://example.com/name> "Tennis" .
<http://example.com/sport/100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .
<http://example.com/student/10> <http://example.com/name> "Venus Williams" .
<http://example.com/student/10> <http://example.com/sport> <http://example.com/sport/100> .
<http://example.com/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
<http://example.com/student/20> <http://example.com/name> "Demi Moore" .
<http://example.com/student/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
```

Both models have all the relations in the baseline and the `type` ones as well. The graph generated by them is essentially the same, and a good approach to the baseline one.

### 10a

#### Baseline

```
<http://example.com/1> <http://example.com/code> "1" .
<http://example.com/1> <http://example.com/iso> "BO" .
<http://example.com/1> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2> <http://example.com/code> "2" .
<http://example.com/2> <http://example.com/iso> "IE" .
<http://example.com/2> <http://example.com/name> "Ireland" .
<http://example.com/3> <http://example.com/code> "3" .
<http://example.com/3> <http://example.com/iso> "MF" .
<http://example.com/3> <http://example.com/name> "Saint Martin (French part)" .

```

#### GPT4o

```
<http://example.org/countries/1> <http://purl.org/dc/terms/identifier> "BO" .
<http://example.org/countries/1> <http://schema.org/identifier> "1" .
<http://example.org/countries/1> <http://schema.org/name> "Bolivia, Plurinational State of" .
<http://example.org/countries/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Country> .
<http://example.org/countries/2> <http://purl.org/dc/terms/identifier> "IE" .
<http://example.org/countries/2> <http://schema.org/identifier> "2" .
<http://example.org/countries/2> <http://schema.org/name> "Ireland" .
<http://example.org/countries/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Country> .
<http://example.org/countries/3> <http://purl.org/dc/terms/identifier> "MF" .
<http://example.org/countries/3> <http://schema.org/identifier> "3" .
<http://example.org/countries/3> <http://schema.org/name> "Saint Martin (French part)" .
<http://example.org/countries/3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Country> .
```
#### Copilot

```
<http://example.org/1> <http://example.org/hasISO3166> "BO" .
<http://example.org/1> <http://example.org/hasName> "Bolivia, Plurinational State of" .
<http://example.org/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Country> .
<http://example.org/2> <http://example.org/hasISO3166> "IE" .
<http://example.org/2> <http://example.org/hasName> "Ireland" .
<http://example.org/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Country> .
<http://example.org/3> <http://example.org/hasISO3166> "MF" .
<http://example.org/3> <http://example.org/hasName> "Saint Martin (French part)" .
<http://example.org/3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Country> .
```
Both make a good first approach even though the `type` relations aren't reflected. 

### 11b

#### Baseline

```
<http://example.com/student/10> <http://example.com/lastName> "Williams" .
<http://example.com/student/10> <http://example.com/firstName> "Venus" .
<http://example.com/student/12> <http://example.com/lastName> "Villa" .
<http://example.com/student/12> <http://example.com/firstName> "David" .
<http://example.com/student/11> <http://example.com/lastName> "Alonso" .
<http://example.com/student/11> <http://example.com/firstName> "Fernando" .
<http://example.com/sport/110> <http://example.com/description> "Tennis" .
<http://example.com/sport/110> <http://example.com/id> "110" .
<http://example.com/sport/111> <http://example.com/description> "Football" .
<http://example.com/sport/111> <http://example.com/id> "111" .
<http://example.com/sport/112> <http://example.com/description> "Formula1" .
<http://example.com/sport/112> <http://example.com/id> "112" .
<http://example.com/student/10> <http://example.com/plays> <http://example.com/sport/110> .
<http://example.com/student/12> <http://example.com/plays> <http://example.com/sport/111> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/112> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/111> .
```

#### GPT4o

```
<http://example.org/sport/110> <http://example.org/description> "Tennis" .
<http://example.org/sport/110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Sport> .
<http://example.org/sport/111> <http://example.org/description> "Football" .
<http://example.org/sport/111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Sport> .
<http://example.org/sport/112> <http://example.org/description> "Formula1" .
<http://example.org/sport/112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Sport> .
<http://example.org/student/10> <http://example.org/firstName> "Venus" .
<http://example.org/student/10> <http://example.org/lastName> "Williams" .
<http://example.org/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
<http://example.org/student/11> <http://example.org/firstName> "Fernando" .
<http://example.org/student/11> <http://example.org/lastName> "Alonso" .
<http://example.org/student/11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
<http://example.org/student/12> <http://example.org/firstName> "David" .
<http://example.org/student/12> <http://example.org/lastName> "Villa" .
<http://example.org/student/12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Student> .
```
#### Copilot

```
<http://example.com/sport/110> <http://example.com/description> "Tennis" .
<http://example.com/sport/110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .
<http://example.com/sport/111> <http://example.com/description> "Football" .
<http://example.com/sport/111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .
<http://example.com/sport/112> <http://example.com/description> "Formula1" .
<http://example.com/sport/112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .
<http://example.com/student/10> <http://example.com/firstName> "Venus" .
<http://example.com/student/10> <http://example.com/isEnrolledIn> <http://example.com/sport/110> .
<http://example.com/student/10> <http://example.com/lastName> "Williams" .
<http://example.com/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
<http://example.com/student/11> <http://example.com/firstName> "Fernando" .
<http://example.com/student/11> <http://example.com/isEnrolledIn> <http://example.com/sport/111> .
<http://example.com/student/11> <http://example.com/isEnrolledIn> <http://example.com/sport/112> .
<http://example.com/student/11> <http://example.com/lastName> "Alonso" .
<http://example.com/student/11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
<http://example.com/student/12> <http://example.com/firstName> "David" .
<http://example.com/student/12> <http://example.com/isEnrolledIn> <http://example.com/sport/111> .
<http://example.com/student/12> <http://example.com/lastName> "Villa" .
<http://example.com/student/12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
```
The baseline doesn't reflect the `type` relations, but both models do it. GPT4o is not able to represent the relation between each person and the sport they practise, but Copilot makes an adequate representation.

### 12a

#### Baseline

```
_:BobSmith30 <http://example.com/amount> "30" .
_:BobSmith30 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:SueJones20 <http://example.com/amount> "20" .
_:SueJones20 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

#### GPT4o

```
<http://example.org/Person/Bob_Smith> <http://example.org/hasAmount> "30" .
<http://example.org/Person/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/Person/Bob_Smith> <http://xmlns.com/foaf/0.1/familyName> "Smith" .
<http://example.org/Person/Bob_Smith> <http://xmlns.com/foaf/0.1/givenName> "Bob" .
<http://example.org/Person/Sue_Jones> <http://example.org/hasAmount> "20" .
<http://example.org/Person/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/Person/Sue_Jones> <http://xmlns.com/foaf/0.1/familyName> "Jones" .
<http://example.org/Person/Sue_Jones> <http://xmlns.com/foaf/0.1/givenName> "Sue" .
```
#### Copilot

```
<http://example.com/person/Bob_Smith> <http://example.com/amount> "30" .
<http://example.com/person/Bob_Smith> <http://example.com/fname> "Bob" .
<http://example.com/person/Bob_Smith> <http://example.com/lname> "Smith" .
<http://example.com/person/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Person> .
<http://example.com/person/Sue_Jones> <http://example.com/amount> "20" .
<http://example.com/person/Sue_Jones> <http://example.com/fname> "Sue" .
<http://example.com/person/Sue_Jones> <http://example.com/lname> "Jones" .
<http://example.com/person/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Person> .
<http://example.com/transaction/Bob_Smith_30> <http://example.com/amount> "30" .
<http://example.com/transaction/Bob_Smith_30> <http://example.com/hasReceiver> <http://example.com/person/Bob_Smith> .
<http://example.com/transaction/Bob_Smith_30> <http://example.com/hasSender> <http://example.com/person/Bob_Smith> .
<http://example.com/transaction/Bob_Smith_30> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Transaction> .
<http://example.com/transaction/Sue_Jones_20> <http://example.com/amount> "20" .
<http://example.com/transaction/Sue_Jones_20> <http://example.com/hasReceiver> <http://example.com/person/Sue_Jones> .
<http://example.com/transaction/Sue_Jones_20> <http://example.com/hasSender> <http://example.com/person/Sue_Jones> .
<http://example.com/transaction/Sue_Jones_20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Transaction> .
```
Both models represent more relations than the baseline. GPT4o makes a correct approach but Copilot creates non-existent relations between the nodes that represent transactions.

### 12b

#### Baseline

```
_:BobSmith <http://example.com/city> "London" .
_:BobSmith <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:SueJones <http://example.com/city> "Madrid" .
_:SueJones <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

#### GPT4o

```
<http://example.org/person/Bob_Smith> <http://example.org/hasAmount> "30"^^<http://www.w3.org/2001/XMLSchema#decimal> .
<http://example.org/person/Bob_Smith> <http://example.org/hasFirstName> "Bob" .
<http://example.org/person/Bob_Smith> <http://example.org/hasLastName> "Smith" .
<http://example.org/person/Bob_Smith> <http://example.org/livesIn> "London" .
<http://example.org/person/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/person/Sue_Jones> <http://example.org/hasAmount> "20"^^<http://www.w3.org/2001/XMLSchema#decimal> .
<http://example.org/person/Sue_Jones> <http://example.org/hasFirstName> "Sue" .
<http://example.org/person/Sue_Jones> <http://example.org/hasLastName> "Jones" .
<http://example.org/person/Sue_Jones> <http://example.org/livesIn> "Madrid" .
<http://example.org/person/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
```
#### Copilot

```
<http://example.com/person/Bob_Smith> <http://example.com/amount> "30" .
<http://example.com/person/Bob_Smith> <http://example.com/lives_in> "London" .
<http://example.com/person/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Person> .
<http://example.com/person/Sue_Jones> <http://example.com/amount> "20" .
<http://example.com/person/Sue_Jones> <http://example.com/lives_in> "Madrid" .
<http://example.com/person/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Person> .
```
Both models represent more relations than the baseline and, furthermore, the make correctly the link between de CSV files.

### 15a

#### Baseline

```
<http://example.com/BO> <http://www.w3.org/2000/01/rdf-schema#label> "Bolivia, Plurinational State of"@en .
<http://example.com/BO> <http://www.w3.org/2000/01/rdf-schema#label> "Estado Plurinacional de Bolivia"@es .
<http://example.com/IE> <http://www.w3.org/2000/01/rdf-schema#label> "Ireland"@en .
<http://example.com/IE> <http://www.w3.org/2000/01/rdf-schema#label> "Irlanda"@es .
```

#### GPT4o

```
<http://example.org/country/BO> <http://example.org/ns#code> "BO" .
<http://example.org/country/BO> <http://example.org/ns#name_en> "Bolivia, Plurinational State of" .
<http://example.org/country/BO> <http://example.org/ns#name_es> "Estado Plurinacional de Bolivia" .
<http://example.org/country/BO> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/ns#Country> .
<http://example.org/country/IE> <http://example.org/ns#code> "IE" .
<http://example.org/country/IE> <http://example.org/ns#name_en> "Ireland" .
<http://example.org/country/IE> <http://example.org/ns#name_es> "Irlanda" .
<http://example.org/country/IE> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/ns#Country> .
```
#### Copilot

```
<http://example.org/BO> <http://example.org/name_en> "Bolivia, Plurinational State of" .
<http://example.org/BO> <http://example.org/name_es> "Estado Plurinacional de Bolivia" .
<http://example.org/BO> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Country> .
<http://example.org/IE> <http://example.org/name_en> "Ireland" .
<http://example.org/IE> <http://example.org/name_es> "Irlanda" .
<http://example.org/IE> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Country> .
```

Both models are able to detect that the CSV files represent the same data in different languages, even though they don't use the proper notation used in the baseline.