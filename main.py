from pyscript import document
def general_weighted_average(e):
    # Clear previous results
    document.getElementById("student_info").innerText = ""
    document.getElementById("summary").innerText = ""
    document.getElementById("output").innerText = ""
    document.getElementById("status").innerText = ""
    
    # Get the input values based on the html
    science = document.getElementById("science").value
    math = document.getElementById("math").value
    english = document.getElementById("english").value
    filipino = document.getElementById("filipino").value
    ict = document.getElementById("ict").value
    pe = document.getElementById("pe").value
    first_name = document.getElementById("fname").value
    last_name = document.getElementById("lname").value
    
    try:
        # Convert to numbers
        science = float(science)
        math = float(math)
        english = float(english)
        filipino = float(filipino)
        ict = float(ict)
        pe = float(pe)
        
        # Define subject weights
        units_subject = (5, 3, 2, 1)
        
        # Calculate the weighted average based sa guidelines/example
        weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
        total_units = (5 * 3) + 3 + 2 + 1
        gwa = weighted_sum / total_units
        
        # The summary of grades
        subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
        summary = f"""{subjects[0]}: {science:.0f}
            {subjects[1]}: {math:.0f}
            {subjects[2]}: {english:.0f}
            {subjects[3]}: {filipino:.0f}
            {subjects[4]}: {ict:.0f}
            {subjects[5]}: {pe:.0f}"""
        
        # Display results
        document.getElementById("student_info").innerText = f"Name: {first_name} {last_name}"
        document.getElementById("summary").innerText = summary
        document.getElementById("output").innerText = f"Your general weighted average is {gwa:.2f}"
        
        # Determine pass/fail status
        if gwa >= 75:
            document.getElementById("status").innerText = "✅ Passed"
            document.getElementById("status").className = "passed"
        else:
            document.getElementById("status").innerText = "❌ Failed"
            document.getElementById("status").className = "failed"
            
    except ValueError:
        document.getElementById("output").innerText = "Invalid input. Please enter numeric values for all grades."
        document.getElementById("status").innerText = "Error"
