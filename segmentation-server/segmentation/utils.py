def create_annotation(x, y, width, height, id):
    return {
        "type": "Annotation",
        "body": [
            { 
                "type": "TextualBody", "value": "tag", 
                "purpose": "commenting" 
            },
            { 
                "type": "TextualBody", 
                "value": "tag",
                "purpose": "tagging" 
            }
        ],
        "target": {
            "source": "http://localhost:3000/undefined",
            "selector": {
                "type": "FragmentSelector",
                "conformsTo": "http://www.w3.org/TR/media-frags/",
                "value": f'xywh=pixel:{x},{y},{width},{height}'
            }
        },
        "@context": "http://www.w3.org/ns/anno.jsonld",
        "id": f"{id}"
    }