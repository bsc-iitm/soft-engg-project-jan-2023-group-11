<template>
    <div class="bg">
    <div class="heading">Quick Resolve</div>
    <LoginBox />
    </div>
</template>

<script>
import LoginBox from '@/components/LoginBox.vue'

export default{
    // eslint-disable-next-line
    name : "LoginPage",
    components: { LoginBox }
}
</script>
