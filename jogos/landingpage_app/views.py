from django.shortcuts import render
import requests
from django.shortcuts import redirect  # Importe a função redirect

# ...

def landing_page(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if action == 'signup':
            # Criar novo usuário
            create_user_url = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBNM-RqmvNc-koeOtK2r14pdwl8kpYqonQ'
            data = {
                'email': email,
                'password': password,
                'returnSecureToken': True
            }
            response = requests.post(create_user_url, json=data)
            
            # Tratamento da resposta para a criação de usuário
            response_data = response.json()
            if 'error' in response_data:
                error_message = response_data['error']['message']
                return render(request, './landing_page.html', {'error_message': error_message})
            else:
                # Usuário criado com sucesso
                return redirect('servicojogos')  # Redirecione para a view servicojogos

        elif action == 'login':
            # Fazer login do usuário
            sign_in_url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBNM-RqmvNc-koeOtK2r14pdwl8kpYqonQ'
            data = {
                'email': email,
                'password': password,
                'returnSecureToken': True
            }
            response = requests.post(sign_in_url, json=data)
            # Trate a resposta conforme necessário

            response_data = response.json()
            if 'error' in response_data:
                error_message = response_data['error']['message']
                return render(request, './landing_page.html', {'error_message': error_message})
            else:
                # Usuário autenticado com sucesso
                return redirect('servicojogos')  # Redirecione para a view servicojogos

    return render(request, './landing_page.html')