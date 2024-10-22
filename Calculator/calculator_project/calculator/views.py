from django.shortcuts import render

def calculator(request):
    result = None
    error_message = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'Add':
                result = num1 + num2
            elif operation == 'Subtract':
                result = num1 - num2
            elif operation == 'Multiply':
                result = num1 * num2
            elif operation == 'Divide':
                if num2 == 0:
                    error_message = "Cannot divide by zero!"
                else:
                    result = num1 / num2
            elif operation == 'Mod':
                result = num1 % num2
        except (ValueError, TypeError):
            error_message = "Please enter valid numbers."

    return render(request, 'calculator/calculator.html', {'result': result, 'error_message': error_message})
