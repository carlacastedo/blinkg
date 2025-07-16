| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join Condition | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `stop_id` | `gtfs:id` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | - | `xsd:string` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` |
| `stop_code` | `gtfs:code` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `xsd:string` | - | `{stop_code}` |
| `stop_name` | `gtfs:name` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `foaf:name` | - | `{stop_name}` |
| `stop_desc` | `gtfs:desc` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `xsd:string` | - | `{stop_desc}` |
| `stop_lat` | `gtfs:latitude` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `geo:lat` | - | `{stop_lat}` |
| `stop_lon` | `gtfs:longitude` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `geo:long` | - | `{stop_lon}` |
| `zone_id` | *(not mapped)* | `gtfs:Stop` | `gtfs:Zone` | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `xsd:string` | - | `{zone_id}` |
| `stop_url` | `gtfs:url` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `foaf:page` | - | `{stop_url}` |
| `location_type` | `gtfs:locationType` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `skos:Concept` | `map_location_type` | `http://transport.linkeddata.es/kos/location-type/{location_type}` |
| `parent_station` | `gtfs:parentStation` | `gtfs:Stop` | `gtfs:Station` | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `gtfs:Station` | - | `http://transport.linkeddata.es/id/station/{parent_station}` |
| `stop_timezone` | `gtfs:timezone` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `xsd:string` | - | `{stop_timezone}` |
| `wheelchair_boarding` | `gtfs:wheelchairAccessible` | `gtfs:Stop` | - | `http://transport.linkeddata.es/id/stop/{stop_id}` | `stop_id` | `skos:Concept` | `map_wheelchair_boarding` | `http://transport.linkeddata.es/kos/wheelchair-accesible/{wheelchair_boarding}` |
