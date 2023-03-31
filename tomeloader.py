import folder_paths
import tomesd as ts
import comfy

class CheckpointTomeLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                              "ckpt_name": (folder_paths.get_filename_list("checkpoints"),), 
                              "ratio": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                            }}
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "loaders"

    def load_checkpoint(self, ckpt_name, ratio, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        modelpatcher, clip, vae = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        
        print("Printing Tomesd module...")
        print(type(modelpatcher.model))
        print(dir(ts))
        ts.apply_patch(modelpatcher.model,ratio=ratio)

        return (modelpatcher, clip, vae)

class TestNode:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                #"wildcard_name": (folder_paths.get_filename_list("wildcard_text")),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello World!"
                }),
            },

        }

    RETURN_TYPES = ("string")
    FUNCTION = "get_random_line"

    #OUTPUT_NODE = False

    CATEGORY = "custom"

    def get_random_line(self, string_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
            """)
        return ("string output",)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "TestNode": TestNode,
    "CheckpointTomeLoader":CheckpointTomeLoader
}
