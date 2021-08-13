#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor


class AIEngine:

    @classmethod
    def detect_labels(cls, photo, bucket, target, print_labels=False, show_boxes=False) -> bool:

        client = boto3.client('rekognition')
        response = client.detect_labels(Image={'S3Object':{'Bucket': bucket, 'Name': photo}}, MaxLabels=10)
        
        s3_connection = boto3.resource('s3')
        s3_object = s3_connection.Object(bucket, photo)
        s3_response = s3_object.get()
        
        stream = io.BytesIO(s3_response['Body'].read())
        image = Image.open(stream)
        
        imgWidth, imgHeight = image.size
        draw = ImageDraw.Draw(image)

        if print_labels == True:
            print('Detected labels for ' + photo)
            print()
            for label in response['Labels']:
                print ("Label: " + label['Name'])
                print ("Confidence: " + str(label['Confidence']))
                print ("Instances:")
                for instance in label['Instances']:
                    print ("  Bounding box")
                    print ("    Top: " + str(instance['BoundingBox']['Top']))
                    print ("    Left: " + str(instance['BoundingBox']['Left']))
                    print ("    Width: " +  str(instance['BoundingBox']['Width']))
                    print ("    Height: " +  str(instance['BoundingBox']['Height']))
                    print ("  Confidence: " + str(instance['Confidence']))
                    print()

                print ("Parents:")
                for parent in label['Parents']:
                    print ("   " + parent['Name'])
                print ("----------")
                print ()
        
        if show_boxes == True:
            for label in response['Labels']:
                if label['Name'] == 'Cat' or label['Name'] == 'Dog':
                    for instance in label['Instances']:
                        box = instance['BoundingBox']
                        left = imgWidth * box['Left']
                        top = imgHeight * box['Top']
                        width = imgWidth * box['Width']
                        height = imgHeight * box['Height']

                        points = (
                            (left,top),
                            (left + width, top),
                            (left + width, top + height),
                            (left , top + height),
                            (left, top)
                        )
                        draw.line(points, fill='#00d400', width=2)
                        image.show()
            image.close()

        labels = []
        for item in response['Labels']:
            labels.append((item['Name'], item['Confidence']))

        res = False
        for l in labels:
            if l[0] in target and l[1] > 0.85:
                res = l[0] in target

        return res
