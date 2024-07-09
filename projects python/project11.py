# import pywhatkit as pw

# txt = """Python is an Language which is easier than C++ and Java.
# Its design philosophy emphasizes code readability with its use"""

# pw.text_to_handwriting(txt,"demo1.png",[255,0,0])
# print("END")

import pywhatkit as kit

import cv2

kit.text_to_handwriting("""Python is an Language which is easier than C++ and Java.
Its design philosophy emphasizes code readability with its use""",save_to="demo.png")

# img = cv2.imread("handwriting.png")
# cv2.imshow("Text to Handwriting", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()