import cv2

def detect_shapes(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
        if len(approx) == 3:
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
            print("Am detectat un triunghi.")
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w)/h
            if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
                print("Am detectat un pătrat.")
            else:
                cv2.drawContours(image, [approx], 0, (255, 0, 0), 2)
                print("Am detectat un dreptunghi.")
        elif len(approx) == 5:
            cv2.drawContours(image, [approx], 0, (0, 0, 255), 2)
            print("Am detectat un pentagon.")
        elif len(approx) == 6:
            cv2.drawContours(image, [approx], 0, (255, 255, 0), 2)
            print("Am detectat un hexagon.")
        elif len(approx) == 7:
            cv2.drawContours(image, [approx], 0, (255, 255, 0), 2)
            print("Am detectat un heptagon.")
        else:
            cv2.drawContours(image, [approx], 0, (128, 128, 128), 2)
            print("Am detectat un poligon cu", len(approx), "laturi.")

    cv2.imshow('Shapes Detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_shapes(r'C:\Users\danie\Desktop\Python\Hexa.png')
