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
        #Changes interaction style to trackball rather than the default click movement
        self.render_window_interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()
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

        self.renderer.SetBackground(bg_color)


    def draw_object(self, obj):

        if(obj.render_object == RenderObjects.frame):

            tmp_transform = vtk.vtkTransform()
            tmp_transform.Translate(obj.origin[0, 0], obj.origin[1, 0], obj.origin[2, 0])
            axes = vtk.vtkAxesActor()
            axes.SetUserTransform(tmp_transform)
            self.renderer.AddActor(axes)

            return axes

        if(obj.render_object == RenderObjects.cube):

            cube = vtk.vtkCubeSource()

            cube.SetXLength(obj.size)
            cube.SetYLength(obj.size)
            cube.SetZLength(obj.size)
            cube.SetCenter(obj.com.v)

            tmp_cube_mapper = vtk.vtkPolyDataMapper()
            tmp_cube_mapper.SetInputConnection(cube.GetOutputPort())
            cube_actor = vtk.vtkActor()
            cube_actor.SetMapper(tmp_cube_mapper)
            cube_actor.GetProperty().SetColor(obj.color)

            self.renderer.AddActor(cube_actor)

            return cube_actor

        if(obj.render_object == RenderObjects.cuboid):

            cuboid = vtk.vtkCubeSource()

            cuboid.SetXLength(obj.size_x)
            cuboid.SetYLength(obj.size_y)
            cuboid.SetZLength(obj.size_z)
            cuboid.SetCenter(obj.com.v)

            tmp_cuboid_mapper = vtk.vtkPolyDataMapper()
            tmp_cuboid_mapper.SetInputConnection(cuboid.GetOutputPort())
            cuboid_actor = vtk.vtkActor()
            cuboid_actor.SetMapper(tmp_cuboid_mapper)
            cuboid_actor.GetProperty().SetColor(obj.color)

            self.renderer.AddActor(cuboid_actor)

            return cuboid_actor

        if(obj.render_object == RenderObjects.sphere):

            sphere = vtk.vtkSphereSource()

            sphere.SetRadius(obj.radius)
            sphere.SetCenter(obj.com.v)
            sphere.SetThetaResolution(obj.theta_resolution)
            sphere.SetPhiResolution(obj.phi_resolution)

            tmp_sphere_mapper = vtk.vtkPolyDataMapper()
            tmp_sphere_mapper.SetInputConnection(sphere.GetOutputPort())
            sphere_actor = vtk.vtkActor()
            sphere_actor.SetMapper(tmp_sphere_mapper)
            sphere_actor.GetProperty().SetColor(obj.color)

            self.renderer.AddActor(sphere_actor)

            return sphere_actor

        if(obj.render_object == RenderObjects.cylinder):

            cylinder = vtk.vtkCylinderSource()

            cylinder.SetRadius(obj.radius)
            cylinder.SetHeight(obj.height)
            cylinder.SetResolution(obj.theta_resolution)

            tmp_cylinder_mapper = vtk.vtkPolyDataMapper()
            tmp_cylinder_mapper.SetInputConnection(cylinder.GetOutputPort())
            cylinder_actor = vtk.vtkActor()
            cylinder_actor.SetMapper(tmp_cylinder_mapper)
            cylinder_actor.GetProperty().SetColor(obj.color)

            self.renderer.AddActor(cylinder_actor)

            return cylinder_actor



















































            


    def render_display(self):

        self.render_window.Render()
        self.render_window_interactor.Start()

    def render(self):
        
        self.render_window.Render()

    def update(self):

        self.render_window.SetSize(self.width, self.height)
        self.renderer.SetBackground(self.colors.GetColor3d("bg_color"))
        

