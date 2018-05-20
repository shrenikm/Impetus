import vtk
import numpy as np 

from .. numeric.constants import RenderObjects

#Class that implements the main Impetuts simulator

class ISimulator(object):

    def __init__(self, width = 600, height = 480, bg_color = [0, 0, 0, 255]):

        self.width = width
        self.height = height

        self.renderer = vtk.vtkRenderer()
        self.render_window = vtk.vtkRenderWindow()
        self.render_window_interactor = vtk.vtkRenderWindowInteractor()
        self.render_window.AddRenderer(self.renderer)
        self.render_window_interactor.SetRenderWindow(self.render_window)

        self.render_window.SetSize(self.width, self.height)

        self.colors = vtk.vtkNamedColors()
        self.colors.SetColor("bg_color", bg_color)
        self.renderer.SetBackground(self.colors.GetColor3d("bg_color"))


    def set_window_size(self, width, height):

        self.width = width
        self.height = height
        self.render_window.SetSize(self.width, self.height)

    def set_background_color(self, bg_color):

        self.renderer.SetBackground(bg_color[0], bg_color[1], bg_color[2])


    def draw_object(self, obj):

        if(obj.render_object == RenderObjects.frame):
            axes = vtk.vtkAxesActor()
            self.renderer.AddActor(axes)



    def render(self):

        self.render_window.Render()
        self.render_window_interactor.Start()

    def update(self):

        self.render_window.SetSize(self.width, self.height)
        self.renderer.SetBackground(self.colors.GetColor3d("bg_color"))
        

