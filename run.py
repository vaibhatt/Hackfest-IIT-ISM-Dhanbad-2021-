from eval import captionize

input_path = r"E:\Projects\Hackfest_IIT_ISM_2021\input_path\cricket.jpg"
output_path = r"E:\Projects\Hackfest_IIT_ISM_2021\output_path\output.mp3"

if __name__=='__main__':
    captionize(input_path,output_path,play_now=True,print_caption=True)


