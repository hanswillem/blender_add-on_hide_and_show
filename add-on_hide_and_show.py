bl_info = {
    'name' : 'Hide & Show',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 80, 0  ),
    'location' : 'View 3D > Tools > My Addon',
    'description' : 'Quickly hide and show objects',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'Hide & Show'
    }


#imports
import bpy

#the main function
def main_hide():
    obs = bpy.context.selected_objects
    bpy.context.scene.frame_current -= 1
    for i in obs:
        i.hide_viewport = False
        i.hide_render = False
        i.keyframe_insert(data_path = 'hide_viewport')
        i.keyframe_insert(data_path = 'hide_render')
    bpy.context.scene.frame_current += 1
    for i in obs:
        i.select_set(True)
        i.hide_viewport = True
        i.hide_render = True
        i.keyframe_insert(data_path = 'hide_viewport')
        i.keyframe_insert(data_path = 'hide_render')

#the main function
def main_show():
    obs = bpy.context.selected_objects
    bpy.context.scene.frame_current -= 1
    for i in obs:
        i.hide_viewport = True
        i.hide_render = True
        i.keyframe_insert(data_path = 'hide_viewport')
        i.keyframe_insert(data_path = 'hide_render')
    bpy.context.scene.frame_current += 1
    for i in obs:
        i.select_set(True)
        i.hide_viewport = False
        i.hide_render = False
        i.keyframe_insert(data_path = 'hide_viewport')
        i.keyframe_insert(data_path = 'hide_render')

#panel class
class HIDESHOW_PT_Panel(bpy.types.Panel):
    #panel attributes
    """Tooltip"""
    bl_label = 'Hide & Show'
    bl_idname = 'HIDESHOW_PT_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Hide & Show'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        col.operator('script.hide', text='Hide after this frame')
        col.operator('script.show', text='Show after this frame')

        
#operator class
class HIDE_OT_Operator(bpy.types.Operator):
    #operator attributes
    """Tooltip"""
    bl_label = 'Hide'
    bl_idname = 'script.hide'
    
    #poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return len(bpy.context.selected_objects) > 0
    
    #execute
    def execute(self, context):
        main_hide()
        return {'FINISHED'}

#operator class
class SHOW_OT_Operator(bpy.types.Operator):
    #operator attributes
    """Tooltip"""
    bl_label = 'Show'
    bl_idname = 'script.show'
    
    #poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return len(bpy.context.selected_objects) > 0
    
    #execute
    def execute(self, context):
        main_show()
        return {'FINISHED'}
    
#registration
classes = (
    HIDESHOW_PT_Panel,
    HIDE_OT_Operator,
    SHOW_OT_Operator,
    MyPropertyGroup
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
#enable to test the addon by running this script
if __name__ == '__main__':
    register()
