import cv2
import imutils

hogcv = cv2.HOGDescriptor()
hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

image = cv2.imread('test6.jpg')
image = imutils.resize(image, width=min(700, image.shape[1]),
                           height=min(525, image.shape[1]))

scrap, weights = hogcv.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(16, 16),
                                            scale=1.07
                                            )

person = 1
for x, y, w, h in scrap:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'person {person}', (x, y),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.62, (0, 0, 255), 1)
        person += 1
cv2.putText(image, f'Number of person: ', (40, 70),
                cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 1)
cv2.putText(image, f'{person - 1}', (305, 70),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)
cv2.imshow('result', image)
print(person)

cv2.waitKey(0)
cv2.destroyAllWindows()

