import React from 'react';
import {useState, useEffect} from 'react'
import * as Annotorious from '@recogito/annotorious-openseadragon';
import SelectorPack from '@recogito/annotorious-selector-pack'
import '@recogito/annotorious-openseadragon/dist/annotorious.min.css';
import { useSelector } from 'react-redux';
import annotationCreator from '../utils/AnnotationCreator';

const Drawer = () => {
    const [anno, setAnno] = useState(null)
    const viewer = useSelector(state => state.viewer)
    const image = useSelector(state => state.image)
    const segments = useSelector(state => state.segments)

    const drawSegmentations = (annotator) => {
        const imageURL = `api/v1/cytology/upload/${image}`
        const annotations = annotationCreator(segments, imageURL)
        annotator.setAnnotations(annotations)
    }

    const initializeAnnotations = (viewer) => {
        anno && anno.destroy()
        const annotateState = Annotorious(viewer, {
            locale: 'auto',
        });

        annotateState.setDrawingTool('polygon')
        drawSegmentations(annotateState)
        setAnno(annotateState)
    }
    useEffect(() => {
        if (viewer) {
            initializeAnnotations(viewer)
        }
    }, [viewer]);

    return (
        <div>
            
        </div>
    );
}

export default Drawer;
