from pyscript import document
import random

def nanamigreen(event):
    answer1 = document.querySelector('input[name="answer1"]:checked')
    answer3 = document.querySelector('input[name="answer3"]:checked')
    grade = document.getElementById("grd").value
    section = document.getElementById("sct").value
    result_element = document.getElementById("Result")
    
    if answer1 and answer3:
        registration_choice = answer1.value
        clearance_choice = answer3.value 
        
        # Check if both are "yes"
        if registration_choice == "yes" and clearance_choice == "yes1":
            # Show random image with associated text
            images_data = {
                "BB.jpg": "Congratulations! You are part of Blue Bears!",
                "RB.jpg": "Congratulations! You are part of Red Buldogs!",
                "YT.jpg": "Congratulations! You are part of Yellow Tigers!",
                "GH.jpg": "Congratulations! You are part of Green Hornets!"
            }
            random_image = random.choice(list(images_data.keys()))
            image_text = images_data[random_image]
            result_element.innerHTML = f'<div style="text-align: center;"><img src="{random_image}" alt="Success" style="max-width: 100%; height: auto; border-radius: 10px;"><p style="margin-top: 15px; font-weight: 600; color: #003366; font-size: 18px;">{image_text}</p></div>'
        else:
            result_element.textContent = "Please register online through the link provided by your advisor & consult the clinic to secure your medical clearance."
    else:
        result_element.textContent = "Please fill the form out completely"