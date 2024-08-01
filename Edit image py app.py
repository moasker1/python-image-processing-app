#===========================================================================================================================================================
from tkinter import Tk, Canvas, filedialog
from tkinter.ttk import Frame, Label, Button, Style
from PIL import ImageTk, Image
import cv2
import numpy as np
#===========================================================================================================================================================

class GUI:
    def __init__(self, master):
        self.master = master
        self.TheMainGUI()
        
    def TheMainGUI(self):
        self.master.geometry('1200x1000')
        self.master.title('Multimedia Project')
        self.master['background']='#856ff8'
#===========================================================================================================================================================        
        self.frame_label = Frame(self.master)
        self.frame_label.pack()
        Label(self.frame_label, text='Multimedia Project', font=('Times', 30), background="#800080", foreground="white").grid(row=0, column=2)        
#===========================================================================================================================================================        
        self.frame_menu = Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(padding=(50, 15))
#===========================================================================================================================================================        
        self.style = Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')
        self.style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])
#===========================================================================================================================================================
        Label(self.frame_menu, text="Tools", font=('Times', 30, "underline", "bold"), foreground="#800080").grid(row=1, column=0, columnspan=2, padx=100, pady=5, sticky='sw')

        Button(self.frame_menu, text="Load & Display", command=self.upload_action).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        Button(self.frame_menu, text="Enhancement Methods", command=self.Enhancement_methods).grid(row=3, column=0, columnspan=2, padx=0, pady=5)
        Button(self.frame_menu, text="Image Segmentation", command=self.segmentation).grid(row=4, column=0, padx=5, pady=5)
        Button(self.frame_menu, text="Image Resize", command=self.resize_action).grid(row=5, column=0, padx=5, pady=5)
        Button(self.frame_menu, text="Save Output", command=self.save_action).grid(row=6, column=0, columnspan=2, padx=0, pady=5)
#===========================================================================================================================================================        
        self.canvas = Canvas(self.frame_menu, bg="#856ff8", width=300, height=400)
        self.canvas.grid(row=0, column=3, rowspan=10)
#===========================================================================================================================================================     
        self.side_frame = Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=4, rowspan=10)
#===========================================================================================================================================================        
        self.apply_and_cancel = Frame(self.master)
        self.apply_and_cancel.pack()
#===========================================================================================================================================================
        Button(self.apply_and_cancel, text="Apply", command=self.apply_action).grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        Button(self.apply_and_cancel, text="Ctrl Z", command=self.cancel_action).grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        Button(self.apply_and_cancel, text="Forget All Changes", command=self.forget_action).grid(row=0, column=2, columnspan=1, padx=5, pady=5)
#===========================================================================================================================================================        

    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)
    
    def save_action(self):
        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type

        save_as_image = self.edited_image
        cv2.imwrite(filename, save_as_image)
        self.filename = filename

    def open_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass

        self.display_image(self.edited_image)
        self.side_frame = Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=4, rowspan=10)
    
    def segmentation(self):
        seg, self.filtered_image = cv2.threshold(
            cv2.cvtColor(self.edited_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)

    def resize_action(self):
        self.filtered_image = cv2.resize(self.edited_image, None, fx=2, fy=2)
        cv2.imshow("after", self.filtered_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def blur_action(self):
        self.filtered_image = cv2.GaussianBlur(self.edited_image, (15, 15), 0)
        self.display_image(self.filtered_image)

#===========================================================================================================================================================

    def Enhancement_methods(self):
        self.open_side_frame()
        Button(self.side_frame, text="Black & White", command=self.bw_action).grid(row=1, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Negative", command=self.negative_action).grid(row=2, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Erosion", command=self.erosion_action).grid(row=3, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Dilation", command=self.dilation_action).grid(row=4, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(row=5, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Rotate", command=self.rotate_action).grid(row=6, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Flip", command=self.flip_action).grid(row=7, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Brightness", command=self.brightness_action).grid(row=8, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Contrast", command=self.contrast_action).grid(row=9, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Edge Detection", command=self.edge_detection_action).grid(row=10, column=2, padx=5, pady=5, sticky='se')
        Button(self.side_frame, text="Gaussian Blur", command=self.blur_action).grid(row=11, column=2, padx=5, pady=5, sticky='se')

    def bw_action(self):
        self.filtered_image = cv2.cvtColor(self.edited_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)

    def erosion_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.erode(self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)

    def dilation_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.dilate(self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)
    
    def negative_action(self):
        self.filtered_image = cv2.bitwise_not(self.edited_image)
        self.display_image(self.filtered_image)

    def sketch_action(self):
        gray_image = cv2.cvtColor(self.edited_image, cv2.COLOR_BGR2GRAY)
        inverted_image = cv2.bitwise_not(gray_image)
        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
        inverted_blurred = cv2.bitwise_not(blurred)
        self.filtered_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)

    def rotate_action(self):
        self.filtered_image = cv2.rotate(self.edited_image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.filtered_image)

    def flip_action(self):
        self.filtered_image = cv2.flip(self.edited_image, 1)
        self.display_image(self.filtered_image)

    def brightness_action(self):
        self.filtered_image = cv2.convertScaleAbs(self.edited_image, alpha=1, beta=50)
        self.display_image(self.filtered_image)

    def contrast_action(self):
        self.filtered_image = cv2.convertScaleAbs(self.edited_image, alpha=2.0, beta=0)
        self.display_image(self.filtered_image)

    def edge_detection_action(self):
        self.filtered_image = cv2.Canny(self.edited_image, 100, 200)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)

#===================================================================================================================================================================
#============================================lower frame methods====================================================================================================    
    def apply_action(self):
        self.edited_image = self.filtered_image
        self.display_image(self.edited_image)

    def cancel_action(self):
        self.display_image(self.edited_image)

    def forget_action(self):
        self.edited_image = self.original_image.copy()
        self.display_image(self.original_image)
#===================================================================================================================================================================    
    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        if height > 400 or width > 300:
            if ratio < 1:
                new_width = 300
                new_height = int(new_width * ratio)
            else:
                new_height = 400
                new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, image=self.new_image)

mainWindow = Tk()
GUI(mainWindow)
mainWindow.mainloop()
