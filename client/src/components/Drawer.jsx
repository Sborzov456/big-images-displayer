import React from 'react';
import {useState, useEffect} from 'react'
import * as Annotorious from '@recogito/annotorious-openseadragon';
import SelectorPack from '@recogito/annotorious-selector-pack'
import '@recogito/annotorious-openseadragon/dist/annotorious.min.css';
import { useSelector } from 'react-redux';
import {BASE_SEGMENTATION_URL} from '../config'

const Drawer = () => {
    const [anno, setAnno] = useState(null)
    const viewer = useSelector(state => state.viewer)

    const initializeAnnotations = (viewer) => {
        anno && anno.destroy()
        const annotateState = Annotorious(viewer, {
            locale: 'auto',
            allowEmpty: true,
            gigapixelMode: true,
            // formatter
        });

        annotateState.on('clickAnnotation', () => {
            console.log('clicked')
        })
        annotateState.on('createAnnotation', () => {
            console.log('create')
            console.log(annotateState.getAnnotations())
        })
        
        // SelectorPack(annotateState, {
        //     tools: ['ellipse']
        //   })
        annotateState.setDrawingTool('rect')
        console.log(BASE_SEGMENTATION_URL)
        annotateState.loadAnnotations(`${BASE_SEGMENTATION_URL}cytology/segmentation?image_id=0&type=cellularity`)
        setAnno(annotateState)
    }

    // const formatter = (annotation) => {
    //     return 'important'
    // }

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
