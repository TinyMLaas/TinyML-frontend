import streamlit as st 

from services import device_service

# Page setup
st.set_page_config(
    page_title='Device',
    page_icon='✅',
    layout='wide'
)

state = st.session_state

def remove_device(*args):
    try:
        device_service.remove(*args)
        st.success("Device removed successfully.")
    except:
        st.error("Could not remove device.")

# List all registered devices
registered_devices = device_service.get_registered_devices()

if registered_devices is None:
    st.warning("No registered devices.")

else:
    st.header("All registered devices")    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    for row in registered_devices.sort_values("id").itertuples():
        index, id, name, connection, installer, compiler, model, description = row
        col = st.columns(10)
        col[0].write(id)
        # make selected device name bold
        if "selected_device" in state and state.selected_device["id"] == id:
            col[1].write("**"+name+"**")
        else:
            col[1].write(name)
            col[2].write(connection)
            col[3].write(installer)
            col[4].write(compiler)
            col[5].write(model)
            col[6].write(description)
            col[7].button("Remove", key=name, on_click=remove_device, args=(str(id))) # args in st.buttons is always a tuple of strings
            col[8].button("Modify", key=f'm_{name}', on_click=None, args=(
                registered_devices, id, name, connection, installer, compiler, model, description))
            col[9].button("Select", key=f"s_{name}", on_click=None, args=(
                id, name, connection, installer, compiler, model, description))


