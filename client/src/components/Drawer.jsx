import React from 'react';
import {useState, useEffect} from 'react'
import * as Annotorious from '@recogito/annotorious-openseadragon';
import SelectorPack from '@recogito/annotorious-selector-pack'
import '@recogito/annotorious-openseadragon/dist/annotorious.min.css';
import { useSelector } from 'react-redux';

const Drawer = () => {
    const [anno, setAnno] = useState(null)
    const viewer = useSelector(state => state.viewer)

    const initializeAnnotations = (viewer) => {
        anno && anno.destroy()
        const annotateState = Annotorious(viewer, {
            locale: 'auto',
            allowEmpty: true,
            gigapixelMode: true,
            formatter
        });

        annotateState.on('clickAnnotation', () => {
            console.log('clicked')
        })
        annotateState.on('createAnnotation', () => {
            console.log('create')
        })
        
        SelectorPack(annotateState, {
            tools: ['ellipse']
          })
        annotateState.setDrawingTool('ellipse')
        setAnno(annotateState)
    }

    const formatter = (annotation) => {
        return 'important'
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
