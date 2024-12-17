# Experiment 2

There are 11 test cases. For each one of them there is a prompt that is inserted in ChatGPT 4o and Microsoft Copilot. This prompt follows the next template.

```
I have these CSV files and I want to build a knowledge graph with all the relations in it using this ontology. Could you make the graph and the corresponding mappings in RML? Make sure you reflect ALL de relations EXPLICITLY.
file1.csv 
Column 1, ..., Column N
...
file2.csv 
Column 1, ..., Column N
...
ontology.ttl
...
```

Both models brought back results for each of the test cases. Every mapping file generated is transformed in the corresponding knowledge graph with RMLMapper. Most of the times the mapping files are not correct, and RMLMapper cannot build the graph. Since the correction of the semantics is the topic of the study, the syntax is corrected manually in these cases. All test cases are classified within four groups that reflect the difficulty level.

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

#### GPT4o

```
<http://example.org/#Venus> <http://example.org/#name> "Venus" .
<http://example.org/#Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

#### Copilot

```
<http://example.org/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
```

### 02a

#### GPT4o

```
<http://example.org/#person10> <http://example.org/#firstname> "Venus" .
<http://example.org/#person10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#person10> <http://example.org/#name> "Venus" .
<http://example.org/#person10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

#### Copilot

```
<http://example.org/student/10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/student/10> <http://example.org/#name> "Venus" .
<http://example.org/student/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

### 04a

#### GPT4o

```
<http://example.org/#Tennis> <http://example.org/#sportname> "Tennis" .
<http://example.org/#Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/#Venus> <http://example.org/#firstname> "Venus" .
<http://example.org/#Venus> <http://example.org/#practises> <http://example.org/#Tennis> .
<http://example.org/#Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

#### Copilot

```
<http://example.org/Tennis> <http://example.org/#sportname> "Tennis" .
<http://example.org/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/Venus> <http://example.org/#name> "Venus" .
<http://example.org/Venus> <http://example.org/#practises> <http://example.org/Tennis> .
<http://example.org/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

### 05a

#### GPT4o

```
<http://example.org/#Person_Bob_Smith> <http://example.org/#firstname> "Bob" .
<http://example.org/#Person_Bob_Smith> <http://example.org/#lastname> "Smith" .
<http://example.org/#Person_Bob_Smith> <http://example.org/#owes> "30.0E0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#Person_Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#Person_Sue_Jones> <http://example.org/#firstname> "Sue" .
<http://example.org/#Person_Sue_Jones> <http://example.org/#lastname> "Jones" .
<http://example.org/#Person_Sue_Jones> <http://example.org/#owes> "20.0E0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#Person_Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

#### Copilot

```
<http://example.org/Bob_Smith> <http://example.org/#firstname> "Bob" .
<http://example.org/Bob_Smith> <http://example.org/#lastname> "Smith" .
<http://example.org/Bob_Smith> <http://example.org/#owes> "30.0E0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/Sue_Jones> <http://example.org/#firstname> "Sue" .
<http://example.org/Sue_Jones> <http://example.org/#lastname> "Jones" .
<http://example.org/Sue_Jones> <http://example.org/#owes> "20.0E0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

### 08a

#### GPT4o

```
<http://example.org/#person_10> <http://example.org/#firstname> "Venus Williams" .
<http://example.org/#person_10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#person_10> <http://example.org/#lastname> "Venus Williams" .
<http://example.org/#person_10> <http://example.org/#name> "Venus Williams" .
<http://example.org/#person_10> <http://example.org/#practises> <http://example.org/#sport_Tennis> .
<http://example.org/#person_10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#sport_Tennis> <http://example.org/#sportname> "Tennis"@en .
<http://example.org/#sport_Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
```

#### Copilot

```
<http://example.org/10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/10> <http://example.org/#name> "Venus Williams" .
<http://example.org/10> <http://example.org/#practises> <http://example.org/Tennis> .
<http://example.org/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/Tennis> <http://example.org/#sportname> "Tennis" .
<http://example.org/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
```

### 09a

#### GPT4o

```
<http://example.org/#Person_10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#Person_10> <http://example.org/#name> "Venus Williams" .
<http://example.org/#Person_10> <http://example.org/#practises> <http://example.org/#Sport_100> .
<http://example.org/#Person_10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#Person_20> <http://example.org/#id> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#Person_20> <http://example.org/#name> "Demi Moore" .
<http://example.org/#Person_20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#Sport_100> <http://example.org/#sportid> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#Sport_100> <http://example.org/#sportname> "Tennis"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/#Sport_100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
```
#### Copilot

```
<http://example.org/10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/10> <http://example.org/#name> "Venus Williams" .
<http://example.org/10> <http://example.org/#practises> <http://example.org/100> .
<http://example.org/10> <http://example.org/#sportid> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/10> <http://example.org/#sportname> "Venus Williams" .
<http://example.org/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/20> <http://example.org/#id> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/20> <http://example.org/#name> "Demi Moore" .
<http://example.org/20> <http://example.org/#sportid> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/20> <http://example.org/#sportname> "Demi Moore" .
<http://example.org/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
```

### 10a

#### GPT4o

```
<http://example.org/#Country_1> <http://example.org/#id> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#Country_1> <http://example.org/#iso3166> "BO" .
<http://example.org/#Country_1> <http://example.org/#name> "Bolivia, Plurinational State of"@en .
<http://example.org/#Country_1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
<http://example.org/#Country_2> <http://example.org/#id> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#Country_2> <http://example.org/#iso3166> "IE" .
<http://example.org/#Country_2> <http://example.org/#name> "Ireland"@en .
<http://example.org/#Country_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
<http://example.org/#Country_3> <http://example.org/#id> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/#Country_3> <http://example.org/#iso3166> "MF" .
<http://example.org/#Country_3> <http://example.org/#name> "Saint Martin (French part)"@en .
<http://example.org/#Country_3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
```

#### Copilot

```
<http://example.org/1> <http://example.org/#id> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/1> <http://example.org/#iso3166> "BO" .
<http://example.org/1> <http://example.org/#name> "Bolivia, Plurinational State of"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
<http://example.org/2> <http://example.org/#id> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/2> <http://example.org/#iso3166> "IE" .
<http://example.org/2> <http://example.org/#name> "Ireland"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
<http://example.org/3> <http://example.org/#id> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/3> <http://example.org/#iso3166> "MF" .
<http://example.org/3> <http://example.org/#name> "Saint Martin (French part)"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
```

### 11b

#### GPT4o

```
<http://example.org/person/10> <http://example.org/#firstname> "Venus" .
<http://example.org/person/10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/person/10> <http://example.org/#lastname> "Williams" .
<http://example.org/person/10> <http://example.org/#practises> <http://example.org/sport/110> .
<http://example.org/person/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/person/11> <http://example.org/#firstname> "Fernando" .
<http://example.org/person/11> <http://example.org/#id> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/person/11> <http://example.org/#lastname> "Alonso" .
<http://example.org/person/11> <http://example.org/#practises> <http://example.org/sport/111> .
<http://example.org/person/11> <http://example.org/#practises> <http://example.org/sport/112> .
<http://example.org/person/11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/person/12> <http://example.org/#firstname> "David" .
<http://example.org/person/12> <http://example.org/#id> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/person/12> <http://example.org/#lastname> "Villa" .
<http://example.org/person/12> <http://example.org/#practises> <http://example.org/sport/111> .
<http://example.org/person/12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/sport/110> <http://example.org/#sportid> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/sport/110> <http://example.org/#sportname> "Tennis"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/sport/110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/sport/111> <http://example.org/#sportid> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/sport/111> <http://example.org/#sportname> "Football"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/sport/111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/sport/112> <http://example.org/#sportid> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/sport/112> <http://example.org/#sportname> "Formula1"^^<http://www.w3.org/2001/XMLSchema#langString> .
<http://example.org/sport/112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
```

#### Copilot

```
<http://example.org/sport110> <http://example.org/#sportid> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/sport110> <http://example.org/#sportname> "Tennis" .
<http://example.org/sport110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/sport111> <http://example.org/#sportid> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/sport111> <http://example.org/#sportname> "Football" .
<http://example.org/sport111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/sport112> <http://example.org/#sportid> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/sport112> <http://example.org/#sportname> "Formula1" .
<http://example.org/sport112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Sport> .
<http://example.org/student10> <http://example.org/#firstname> "Venus" .
<http://example.org/student10> <http://example.org/#id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/student10> <http://example.org/#lastname> "Williams" .
<http://example.org/student10> <http://example.org/#practises> <http://example.org/sport110> .
<http://example.org/student10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/student11> <http://example.org/#firstname> "Fernando" .
<http://example.org/student11> <http://example.org/#id> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/student11> <http://example.org/#lastname> "Alonso" .
<http://example.org/student11> <http://example.org/#practises> <http://example.org/sport111> .
<http://example.org/student11> <http://example.org/#practises> <http://example.org/sport112> .
<http://example.org/student11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/student12> <http://example.org/#firstname> "David" .
<http://example.org/student12> <http://example.org/#id> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.org/student12> <http://example.org/#lastname> "Villa" .
<http://example.org/student12> <http://example.org/#practises> <http://example.org/sport111> .
<http://example.org/student12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

### 12a

#### GPT4o

```
<http://example.org/#PersonBob_Smith> <http://example.org/#firstname> "Bob" .
<http://example.org/#PersonBob_Smith> <http://example.org/#lastname> "Smith" .
<http://example.org/#PersonBob_Smith> <http://example.org/#owes> "30"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#PersonBob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#PersonSue_Jones> <http://example.org/#firstname> "Sue" .
<http://example.org/#PersonSue_Jones> <http://example.org/#lastname> "Jones" .
<http://example.org/#PersonSue_Jones> <http://example.org/#owes> "20"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#PersonSue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

#### Copilot

```
<http://example.org/Bob_Smith> <http://example.org/#firstname> "Bob" .
<http://example.org/Bob_Smith> <http://example.org/#lastname> "Smith" .
<http://example.org/Bob_Smith> <http://example.org/#owes> "30"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/Sue_Jones> <http://example.org/#firstname> "Sue" .
<http://example.org/Sue_Jones> <http://example.org/#lastname> "Jones" .
<http://example.org/Sue_Jones> <http://example.org/#owes> "20"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

### 12b

#### GPT4o
```
<http://example.org/#Person_Bob_Smith> <http://example.org/#firstname> "Bob" .
<http://example.org/#Person_Bob_Smith> <http://example.org/#lastname> "Smith" .
<http://example.org/#Person_Bob_Smith> <http://example.org/#lives> "London" .
<http://example.org/#Person_Bob_Smith> <http://example.org/#owes> "30"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#Person_Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#Person_Sue_Jones> <http://example.org/#firstname> "Sue" .
<http://example.org/#Person_Sue_Jones> <http://example.org/#lastname> "Jones" .
<http://example.org/#Person_Sue_Jones> <http://example.org/#lives> "Madrid" .
<http://example.org/#Person_Sue_Jones> <http://example.org/#owes> "20"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#Person_Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

#### Copilot
```
<http://example.org/#Bob_Smith> <http://example.org/#firstname> "Bob" .
<http://example.org/#Bob_Smith> <http://example.org/#lastname> "Smith" .
<http://example.org/#Bob_Smith> <http://example.org/#lives> <http://example.org/#London> .
<http://example.org/#Bob_Smith> <http://example.org/#owes> "30"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#Bob_Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
<http://example.org/#Sue_Jones> <http://example.org/#firstname> "Sue" .
<http://example.org/#Sue_Jones> <http://example.org/#lastname> "Jones" .
<http://example.org/#Sue_Jones> <http://example.org/#lives> <http://example.org/#Madrid> .
<http://example.org/#Sue_Jones> <http://example.org/#owes> "20"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.org/#Sue_Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Person> .
```

### 15a

#### GPT4o

```
<http://example.org/country/BO> <http://example.org/#iso3166> "BO" .
<http://example.org/country/BO> <http://example.org/#name> "Bolivia, Plurinational State of"@en .
<http://example.org/country/BO> <http://example.org/#name> "Estado Plurinacional de Bolivia"@es .
<http://example.org/country/BO> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
<http://example.org/country/IE> <http://example.org/#iso3166> "IE" .
<http://example.org/country/IE> <http://example.org/#name> "Ireland"@en .
<http://example.org/country/IE> <http://example.org/#name> "Irlanda"@es .
<http://example.org/country/IE> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
```

#### Copilot

```
<http://example.org/BO> <http://example.org/#iso3166> "BO" .
<http://example.org/BO> <http://example.org/#name> "Bolivia, Plurinational State of"@en .
<http://example.org/BO> <http://example.org/#name> "Estado Plurinacional de Bolivia"@es .
<http://example.org/BO> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
<http://example.org/IE> <http://example.org/#iso3166> "IE" .
<http://example.org/IE> <http://example.org/#name> "Ireland"@en .
<http://example.org/IE> <http://example.org/#name> "Irlanda"@es .
<http://example.org/IE> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/#Country> .
```