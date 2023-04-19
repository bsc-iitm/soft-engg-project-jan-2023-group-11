<template>
    <div class="backdrop">
        <div class="modal">
            <h1>{{ header }}</h1>
            <p>modal content</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ['header'],
}
</script>


<style>
    .modal{
        width: 400px;
        padding: 20px;
        margin: 100px auto;
        background: white;
        border-radius: 10px;
    }
    .backdrop{
        top: 0;
        position: fixed;
        background: rgba(0,0,0,0.5);
        width: 100vw;
        height: 100vh;
    }
</style>