import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import { useDispatch } from "react-redux";

const SelectImage = () => {
    const dispatch = useDispatch()

    const upload = (event) => {
        const file = event.target.files[0]
        const formData = new FormData()
        formData.append('image_file', file)
        formData.append('image_file_name', file.name)
        fetch('http://localhost:8007/api/v1/cytology/upload', {
            method: 'POST',
            "Content-Type": "multipart/form-data",
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            console.log(result['image_file'])
            dispatch({type: 'UPDATE_IMAGE', payload: result['image_file_name']})
            dispatch({type: 'UPDATE_SEGMENTS', payload: result['segmentations']})
        })
    }

    return (
        <Stack direction="row" alignItems="center" spacing={2} style={{margin: 20}}>
            <Button variant="contained" component="label">
                Upload
                <input onChange={upload} hidden multiple type="file"/>
            </Button>
        </Stack>
    );
}

export default SelectImage;
