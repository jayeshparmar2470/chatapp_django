from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404  ## for retriving message to delete it


def favicon(request):
    # Handle favicon request here (e.g., return an empty response)
    return HttpResponse(status=204)  # No content


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username'].upper()

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    if request.method == 'POST': 
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        # return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})



def delete_message(request, message_id):
    # Retrieve the message by its ID
    message = get_object_or_404(Message, id=message_id)

    # Check if the current user is the owner of the message (you may need to adjust this logic)
    if message.user == request.user:
        message.delete()
        return JsonResponse({'success': True, 'message': 'Message deleted successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'You do not have permission to delete this message'})
