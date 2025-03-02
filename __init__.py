import fiftyone.operators as foo
import fiftyone.operators.types as types
import fiftyone as fo


_LOCATIONS = ['Chicago','Denver','Columbus','Houston','Boston','Los Angeles']


class EditMetadata(foo.Operator):

    @property
    def config(self):
        return foo.OperatorConfig(
            name="edit_metadata",
            label="Edit custom metadata",
            dynamic=True,
        )


    def resolve_input(self, ctx):

        inputs = types.Object()
        place_selector = types.AutocompleteView()
        for key in _LOCATIONS:
            place_selector.add_choice(key, label=key)

        inputs.enum(
            "location",
            place_selector.values(),
            required=True,
            label="Station",
            description="Select a location",
            view=place_selector,
        )

        inputs.bool(
            "hazard_detected",
            default=False,
            required=True,
            label="Hazard detected?",
            view=types.CheckboxView(),
        )

        inputs.str(
            "field_notes",
            required=False,
            label="Field Notes",
            description="Freeform notes from the field operator",
        )

        return types.Property(
            inputs, view=types.View(label="Custom Metadata")
        )


    def execute(self, ctx):
        dataset = ctx.dataset
        selected = ctx.selected
        if selected:
            view = dataset.select(selected)
        else:
            view = ctx.view

        set_val = ctx.params.get('location',None)
        set_val = [set_val]*len(view)
        view.set_values('location',set_val)

        set_val = ctx.params.get('hazard_detected',None)
        set_val = [set_val]*len(view)
        view.set_values('hazard_detected',set_val)

        set_val = ctx.params.get('field_notes',None)
        set_val = [set_val]*len(view)
        view.set_values('field_notes',set_val)

        ctx.ops.reload_dataset()
        
        return {"updated": len(view)}


    def resolve_output(self, ctx):
        return None


def register(p):
    p.register(EditMetadata)
