# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def main(fileName):

    bucket = 'ccphotobucket'
    collectionId = 'FaceCollection'
    #fileName = 'hyeri_2.png'
    threshold = 70
    maxFaces = 2

    client = boto3.client('rekognition')

    try:
        response = client.search_faces_by_image(CollectionId=collectionId,
                                                Image={'S3Object': {'Bucket': bucket, 'Name': fileName}},
                                                FaceMatchThreshold=threshold,
                                             MaxFaces=maxFaces)

        faceMatches = response['FaceMatches']

        print('출석체크 프로그램')
        for match in faceMatches:
            print('학생 ID: ' + match['Face']['FaceId'])
            print('유사도: ' + "{:.2f}".format(match['Similarity']) + "%")
    except:
        print("매치되는 얼굴이 없습니다")
