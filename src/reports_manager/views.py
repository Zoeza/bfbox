from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from .models import UploadTemplate
from clients.functions import serial_number_generator



