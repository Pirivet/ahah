image = cv.2.imread('7_v1.png.')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

x = image.reshape(-1, size)
ans = model.predict(x)

print('ероятности принадлежности к разным классам', ans)
print('Ответ: ', np.argmax(ans))
