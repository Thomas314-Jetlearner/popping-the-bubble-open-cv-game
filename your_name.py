# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("B&W Camera", gray)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     colourful = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     cv2.imshow("Camera", gray)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2

# cap = cv2.VideoCapture(0)


# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Error: Could not read frame.")
#         break
#     colourful = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     cv2.waitKey(10) 

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


#     cv2.imshow("Camera", colourful,gray)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     colourful = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     cv2.imshow("Gray", gray)
#     cv2.imshow("HSV", colourful)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()












import cv2

cap = cv2.VideoCapture(0)


while True: 
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inv =  255 - gray
    blur = cv2.GaussianBlur(inv, (25, 25), 0) 
    div = cv2.divide(gray, 255 - blur, scale=256)

    # div_color = cv2.cvtColor(div, cv2.COLOR_GRAY2BGR)
    # div_color[:, :, 0] = div
    # div_color[:, :, 1] = 0
    # div_color[:, :, 2] = div

    cv2.imshow("Pencil Sketch",div )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows
    


    














































