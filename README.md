# BLINKG: A Benchmark for the Automation of Knowledge Graph Construction 

We present BLINKG, a benchmark for testing the capabilities of automatic solutions for the construction of
knowledge graphs from (semi)structured data. It provides:

- **Realistic scenarios**: A suite of progressively complex use cases, drawn from real-world data integration tasks, that challenge automatic solutions to align source fields with ontology concepts.

- **Standardized evaluation**: Clear metrics and gold-standard mappings to quantify precision, recall and overall mapping quality.

- **Extensible framework**: Standard data formats and evaluation scripts so that researchers can plug in new models, prompts or data sources in minutes.



## Benchmark Resources
We have divided the benchmark en three different scenarios, increasing their complexity. They can be found in the folder `scenarios`:

### Scenario 1: Schema-Aligned Mapping
The structure and vocabulary of the input data closely match the target ontology. Mapping tasks involve straightforward identification of classes, properties, and entities. This scenario represents low-complexity environments where LLMs can operate with minimal ambiguity.

### Scenario 2: Functional and Partially Aligned Mapping
Input data includes functional transformations and moderate divergence from the ontology schema. Tasks require interpreting formatting, value normalization, and simple logic operations. It models real-world cases with medium complexity in mapping design.

### Scenario 3: Schema-Distant and High Abstraction Mapping
Input schemas and ontologies have minimal structural or lexical overlap. Tasks demand abstraction, contextual reasoning, and domain understanding to derive correct mappings. This scenario simulates the most challenging conditions for semantic alignment.


## Benchmark Metrics

### Cell similarity 
To assess the quality of the mappings produced by LLMs, we define a flexible and task-sensitive evaluation metric based on semantic similarity. Instead of relying solely on exact string matches, which often fail to recognize paraphrases or synonymous terms, we compute three complementary similarity scores between predicted and reference values:
- Levenshtein distance (normalized): captures character-level similarity.
- Cosine similarity over raw embeddings: using SBERT or any similar LM to compare textual outputs semantically.
- Cosine similarity over ontology verbalizations: comparing descriptions or labels of ontology elements.

For each cell in a predicted table, the metric selects the maximum similarity among these three and compares it against a threshold τ. If the score exceeds the threshold, the annotation is marked as correct. This allows the metric to be robust across tasks of varying complexity—such as class matching, datatype identification, or join condition specification—while remaining sensitive to lexical variation.

### Row matchting
Before evaluating the predicted tables, each generated row must be aligned with the corresponding gold standard row. Since LLMs may reorder or transform input data, a direct row-by-row comparison is unreliable. To address this, we implement a semantic row matching step.
The primary matching criterion is the Ontology Property, as it usually contains uniquely identifying values per row. We compute similarity using multiple measures (Levenshtein distance, embedding-based cosine similarity, and ontology verbalization similarity) to find the closest match.
If the Ontology Property is ambiguous or insufficiently discriminative (e.g., contains repeated or noisy values), we fall back to a composite key using Entity Class and Data Reference, which we identified empirically as the most informative pair of fields across scenarios.
This step ensures that each predicted row is compared against the most appropriate reference, minimizing false negatives due to misalignment.


## Results

Results of our experimental evaluation can be found in `evaluation`. We evaluated six different LLMs: 
Deepseek, Gemini 2.5 pro, GPT-4 Omni, LLama-3.3-70B, Mixtral 8x22B and OpenAI o3. 


## Authors

- David Chaves-Fraga (main contact) - david.chaves at usc.es
- Carla Castedo


CiTIUS - University of Santiago de Compostela, July 2025 - Present
