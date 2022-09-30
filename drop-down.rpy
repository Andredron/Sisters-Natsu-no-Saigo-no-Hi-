init python:

    @renpy.pure
    class DropDown(Action):
        """
        This is an action that displays a drop-down menu based on the labels
        and actions given to it as arguments. This takes an even number of
        arguments, with arguments grouped into pairs.

        `odd arguments`
            The first, third, fifth, and other odd numbered arguments are the
            labels for the drop-down menu, expected to be strings.

        `even arguments`
            The second, fourth, sixth, and other even numbered arguments are
            the actions to be taken when the corresponding label is selected.
        """

        def __init__(self, *args):

            # Group the arguments into pairs.
            labels = args[0::2]
            actions = args[1::2]
            self.entries = list(zip(labels, actions))

        def __call__(self):

            # When activated, capture the focus, then show the drop down screen.
            renpy.capture_focus("dropdown")
            renpy.show_screen("dropdown", entries=self.entries)
            renpy.restart_interaction()


# This screen displays a drop-down menu.
screen dropdown(entries):

    # Show the drop-down menu above everything else.
    zorder 999

    # If the player clicks outside the drop-down menu, hide it.
    dismiss:
        action Hide()

    # Display the menu near the button that caused it to display.
    nearrect:
        focus "dropdown"

        # The actual menu itself, built out of frames and buttons.
        frame:
            style "empty"
            background "#202020"

            has vbox

            for label, action in entries:

                # The button itself. The Hide action hides this menu when the
                # button is clicked.
                textbutton label:
                    action [ Hide(), action ]