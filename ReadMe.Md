## usage

Run this python script in the ollama data path and generate a zip contained all models. This project use it to install models for another computer offline.

```
    python pak.py llama3 latest output_path
```

Result like this
```
{'schemaVersion': 2, 'mediaType': 'application/vnd.docker.distribution.manifest.v2+json', 'config': {'mediaType': 'application/vnd.docker.container.image.v1+json', 'digest': 'sha256:db46ef36ef0b904f8505b1f659ca52384c05c5d29657ca503a2ad053c4817117', 'size': 483}, 'layers': [{'mediaType': 'application/vnd.ollama.image.model', 'digest': 'sha256:00e1317cbf74d901080d7100f57580ba8dd8de57203072dc6f668324ba545f29', 'size': 4661211328}, {'mediaType': 'application/vnd.ollama.image.license', 'digest': 'sha256:4fa551d4f938f68b8c1e6afa9d28befb70e3f33f75d0753248d530364aeea40f', 'size': 12403}, {'mediaType': 'application/vnd.ollama.image.template', 'digest': 'sha256:8ab4849b038cf0abc5b1c9b8ee1443dca6b93a045c2272180d985126eb40bf6f', 'size': 254}, {'mediaType': 'application/vnd.ollama.image.params', 'digest': 'sha256:c0aac7c7f00d8a81a8ef397cd78664957fbe0e09f87b08bc7afa8d627a8da87f', 'size': 128}]}
['_data/models/manifests/registry.ollama.ai/library/llama3/latest', '_data/models/blobs/sha256:db46ef36ef0b904f8505b1f659ca52384c05c5d29657ca503a2ad053c4817117', '_data/models/blobs/sha256:00e1317cbf74d901080d7100f57580ba8dd8de57203072dc6f668324ba545f29', '_data/models/blobs/sha256:4fa551d4f938f68b8c1e6afa9d28befb70e3f33f75d0753248d530364aeea40f', '_data/models/blobs/sha256:8ab4849b038cf0abc5b1c9b8ee1443dca6b93a045c2272180d985126eb40bf6f', '_data/models/blobs/sha256:c0aac7c7f00d8a81a8ef397cd78664957fbe0e09f87b08bc7afa8d627a8da87f']
start zip file
zip over
```
and we get a file named "llama_latest.zip".