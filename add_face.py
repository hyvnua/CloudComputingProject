import boto3
#import cv2
def add_faces_to_collection(bucket, photo, collection_id):
    client = boto3.client('rekognition')

    response = client.index_faces(CollectionId=collection_id,
                                  Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                  ExternalImageId=photo,
                                  MaxFaces=1,
                                  QualityFilter="AUTO",
                                  DetectionAttributes=['ALL'])

    print('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print('  Face ID: ' + faceRecord['Face']['FaceId'])
        print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    return len(response['FaceRecords'])


def main(photo):
    bucket = 'ccphotobucket'
    collection_id = 'FaceCollection'
    #photo = cv2.imread(p)
    #print(photo)
    
    try:
        indexed_faces_count = add_faces_to_collection(bucket, photo, collection_id)
        print("Faces indexed count: " + str(indexed_faces_count))
    
    except:
        print("매치되는 얼굴이 없습니다")


if __name__ == "__main__":
    main()